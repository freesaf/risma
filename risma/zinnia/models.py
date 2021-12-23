#-*- coding: utf-8 -*-
"""Models of Zinnia"""
import cStringIO
import warnings
from datetime import datetime, timedelta
from PIL import Image
import simplejson
import urllib
import urllib2
from urlparse import urlparse

from django.core.files import File
from django.db import models
from django.db.models import Q
from django.utils.html import strip_tags
from django.utils.html import linebreaks
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.utils.importlib import import_module
from django.contrib import comments
from django.contrib.comments.models import CommentFlag
from django.contrib.comments.moderation import moderator
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _

from django.contrib.markup.templatetags.markup import markdown
from django.contrib.markup.templatetags.markup import textile
from django.contrib.markup.templatetags.markup import restructuredtext

import mptt
from tagging.fields import TagField

from settings import settings as root_settings
from zinnia.settings import UPLOAD_TO
from zinnia.settings import MARKUP_LANGUAGE
from zinnia.settings import ENTRY_TEMPLATES
from zinnia.settings import ENTRY_BASE_MODEL
from zinnia.settings import MARKDOWN_EXTENSIONS
from zinnia.settings import AUTO_CLOSE_COMMENTS_AFTER
from zinnia.managers import entries_published, EntryPublishedManager
from zinnia.managers import AuthorPublishedManager
from zinnia.managers import DRAFT, HIDDEN, PUBLISHED
from zinnia.moderator import EntryCommentModerator
from zinnia.url_shortener import get_url_shortener
from zinnia.signals import ping_directories_handler
from zinnia.signals import ping_external_urls_handler

from utils import *


class Author(User):
    """Proxy Model around User"""

    ojts = models.Manager()
    published = AuthorPublishedManager()

    def entries_published(self):
        """Return only the entries published"""
        return entries_published(self.entries)

    @models.permalink
    def get_absolute_url(self):
        """n author's URL"""
        return ('zinnia_author_detail', (self.username,))

    class Meta:
        app_label = string_with_title("zinnia", "Blog")
        """Author's Meta"""
        proxy = True


class Category(models.Model):
    """Category object for Entry"""

    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(help_text=_('used for publication'),
                            unique=True, max_length=255)
    description = models.TextField(_('description'), blank=True)

    parent = models.ForeignKey('self', null=True, blank=True,
                               verbose_name=_('parent category'),
                               related_name='children');
    image = models.ImageField(upload_to=UPLOAD_TO, null=True, blank=True)
    #ordre = models.IntegerField(default=0)
    def entries_published(self):
        """Return only the entries publihed"""
        return entries_published(self.entries)

    @property
    def tree_path(self):
        """Return category's te path, by his ancestors"""
        if self.parent:
            return '%s/%s' % (self.parent.tree_path, self.slug)
        return self.slug

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        """Return category's URL"""
        return ('zinnia_category_detail', (self.tree_path,))

    class Meta:
        app_label = string_with_title("zinnia", "Blog")
        """Category's Meta"""
        ordering = ['title']
        verbose_name = _('category')
        verbose_name_plural = _('categories')

class EntryAbstractClass(models.Model):
    """Base Model design for publishing entries"""
    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (HIDDEN, _('hidden')),
                      (PUBLISHED, _('published')))

    title = models.CharField(_('title'), max_length=255)

    """
    media_principal_1 = models.OneToOneField("ContenuMedia", null=True, blank=True,
                                             related_name='media_principal1')
    media_principal_2 = models.OneToOneField("ContenuMedia", null=True, blank=True,
                                             related_name='media_principal2')
    """                                          
    content = models.TextField(_('content'))
    excerpt = models.TextField(_('excerpt'), blank=True,
                                help_text=_('optional element'))

    tags = TagField(_('tags'))
    categories = models.ManyToManyField(Category, verbose_name=_('categories'),
                                        related_name='entries',
                                        blank=True, null=True)
    related = models.ManyToManyField('self', verbose_name=_('related entries'),
                                     blank=True, null=True)

    slug = models.SlugField(help_text=_('used for publication'),
                            unique_for_date='creation_date',
                            max_length=255)

    authors = models.ManyToManyField(User, verbose_name=_('authors'),
                                     related_name='entries',
                                     blank=True, null=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    featured = models.BooleanField(_('featured'), default=False)
    comment_enabled = models.BooleanField(_('comment enabled'), default=True)
    pingback_enabled = models.BooleanField(_('linkback enabled'), default=True)

    creation_date = models.DateTimeField(_('creation date'),
                                         default=datetime.now)
    last_update = models.DateTimeField(_('last update'), default=datetime.now)
    start_publication = models.DateTimeField(_('start publication'),
                                             help_text=_('date start publish'),
                                             default=(datetime.now() - timedelta(hours=4)))
    end_publication = models.DateTimeField(_('end publication'),
                                           help_text=_('date end publish'),
                                           default=datetime(2042, 3, 15))

    #sites = models.ManyToManyField(Site, verbose_name=_('sites publication'),
    #                               related_name='ent    
    login_required = models.BooleanField(
        _('login required'), default=False,
        help_text=_('only authenticated users can view the entry'))
    password = models.CharField(
        _('password'), max_length=50, blank=True,
        help_text=_('protect the entry with a password'))

    template = models.CharField(
        _('template'), max_length=250,
        default='zinnia/entry_detail.html',
        choices=[('zinnia/entry_detail.html', _('Default template'))] + \
        ENTRY_TEMPLATES,
        help_text=_('template used to display the entry'))

    objects = models.Manager()
    published = EntryPublishedManager()
    search_field = models.TextField(null=True, editable=False)
    
    def save(self, *args, **kwargs):
        #Populating a search field to receive "html-less" code 
        self.search_field = strip_tags(self.content)
        super(EntryAbstractClass, self).save(*args, **kwargs)
        
    @property
    def html_content(self):
        """Return the content correctly formatted"""
        if MARKUP_LANGUAGE == 'markdown':
            return markdown(self.content, MARKDOWN_EXTENSIONS)
        elif MARKUP_LANGUAGE == 'textile':
            return textile(self.content)
        elif MARKUP_LANGUAGE == 'restructuredtext':
            return restructuredtext(self.content)
        elif not '</p>' in self.content:
            return linebreaks(self.content)
        return self.content

    @property
    def previous_entry(self):
        """Return the previous entry"""
        entries = Entry.published.filter(
            creation_date__lt=self.creation_date)[:1]
        if entries:
            return entries[0]

    @property
    def next_entry(self):
        """Return the next entry"""
        entries = Entry.published.filter(
            creation_date__gt=self.creation_date).order_by('creation_date')[:1]
        if entries:
            return entries[0]

    @property
    def word_count(self):
        """Count the words of an entry"""
        return len(strip_tags(self.html_content).split())

    @property
    def is_actual(self):
        """Check if an entry is within publication period"""
        now = datetime.now()
        return now >= self.start_publication and now < self.end_publication

    @property
    def is_visible(self):
        """Check if an entry is visible on site"""
        return self.is_actual and self.status == PUBLISHED

    @property
    def related_published(self):
        """Return only related entries published"""
        return entries_published(self.related)

    @property
    def discussions(self):
        """Return published discussions"""
        return comments.get_model().objects.for_model(
            self).filter(is_public=True)

    @property
    def comments(self):
        """Return published comments"""
        return self.discussions.filter(Q(flags=None) | Q(
            flags__flag=CommentFlag.MODERATOR_APPROVAL))

    @property
    def pingbacks(self):
        """Return published pingbacks"""
        return self.discussions.filter(flags__flag='pingback')

    @property
    def trackbacks(self):
        """Return published trackbacks"""
        return self.discussions.filter(flags__flag='trackback')

    @property
    def comments_are_open(self):
        """Check if comments are open"""
        if AUTO_CLOSE_COMMENTS_AFTER and self.comment_enabled:
            return (datetime.now() - self.start_publication).days < \
                   AUTO_CLOSE_COMMENTS_AFTER
        return self.comment_enabled

    @property
    def short_url(self):
        """Return the entry's short url"""
        return get_url_shortener()(self)

    def __unicode__(self):
        return '%s: %s' % (self.title, self.get_status_display())

    @models.permalink
    def get_absolute_url(self):
        """Return entry's URL"""
        return ('zinnia_entry_detail', (), {
            'year': self.creation_date.strftime('%Y'),
            'month':self.creation_date.strftime('%m'),
            'day': self.creation_date.strftime('%d'),
            'slug': self.slug})
    
    @property
    def contenu_media1(self):
        try:
            return self.entry_media_principal1
        except:
            return None
    
    @property
    def contenu_media2(self):
        try:
            return self.entry_media_principal2
        except:
            return None        
 
    @property
    def link(self):
        return root_settings.SITE_URL + self.get_absolute_url()
       
    class Meta:
        app_label = string_with_title("zinnia", "Blog")
        abstract = True


def get_base_model():
    """Determine he bas el to inherit in the
    Entry Model, this allow to overload it."""
    if not ENTRY_BASE_MODEL:
        return EntryAbstractClass

    module_name = ENTRY_BASE_MODEL[:dot]
    class_name = ENTRY_BASE_MODEL[dot + 1:]
    try:
        _class = getattr(import_module(module_name), class_name)
        return _class
    except (ImportError, AttributeError):
        warnings.warn('%s cannot be imported' % ENTRY_BASE_MODEL,
                      RuntimeWarning)
    return EntryAbstractClass


class Entry(get_base_model()):
    """Final Entry model"""

    class Meta:
        app_label = string_with_title("zinnia", "Blog")
        """Entry's Meta"""
        ordering = ['-creation_date']
        verbose_name = _('entry')
        verbose_name_plural = _('entries')
        permissions = (('can_view_all', 'Can view all'),
                       ('can_change_author', 'Can change author'), )


class EntryNombreLus(models.Model):
    entry = models.ForeignKey(Entry)
    date_consultation = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        return u"%s lu à %s" % (self.entry.pk, self.date_consultation)
    
    
class ContenuMedia(models.Model):
    """ Contenu media qui va avec le post (image, vidéo ou audio)."""
    entry = models.ForeignKey(Entry,editable=False, null=True)
    media_principal1 = models.OneToOneField(Entry, null=True, editable=False,
                                             related_name='entry_media_principal1')
    media_principal2 = models.OneToOneField(Entry, null=True, editable=False,
                                             related_name='entry_media_principal2')
    image = models.ImageField(upload_to=UPLOAD_TO, null=True, blank=True)    
    video = models.URLField(_(u'Vidéo'), null=True, blank=True, 
                        help_text=u"Fournir URL d'une vidéo provenant de Youtube/Dailymotion ou Vimeo")
    old_url = models.CharField(max_length=250, editable=False, null=True)
    titre = models.CharField(max_length=250, editable=False, null=True)
    thumbnail_url = models.ImageField(upload_to=UPLOAD_TO, null=True, blank=True, editable=False)    
    integration = models.TextField(null=True, blank=True)
        
    def __unicode__(self):
        return self.type_media
    
    @property
    def contenu(self):
        if not self.image and not self.integration:
            """Si l'utilisateur vide tous les champs image et intégration
            on supprime."""
            self.delete()
            return
        return self.integration or self.image
    
    @property    
    def type_media(self):
        if self.integration:
            return u"embeded"
        else:
            return u"image"
        
    @property
    def miniature(self):
        if self.image:
            return self.image
        if self.thumbnail_url:
            return self.thumbnail_url
        return False
                 
    def save(self, *args, **kwargs):
        if self.video != self.old_url and len(self.video) > 0:
            url=""
            scheme, domain, path, params, query, fragment = urlparse(self.video)
            if "dailymotion.com" in domain:
                url = "http://www.dailymotion.com/services/oembed?format=json&%s" % urllib.urlencode({"url": self.video})
            elif "youtube.com" in domain:
                url = "http://www.youtube.com/oembed?format=json&%s" % urllib.urlencode({"url": self.video})
            elif "vimeo.com" in domain:
                url = "http://vimeo.com/api/oembed.json?%s" % urllib.urlencode({"url": self.video})
            
            headers = {'User-Agent':  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            req = urllib2.Request(url, "", headers)
            obj = simplejson.loads(urllib2.urlopen(req).read())
            self.integration = obj.get("html", None)
            
            image_url = obj.get("thumbnail_url", None)
            name = urlparse(image_url)[2].split('/')[-1]            
            file = urllib.urlopen(image_url)
            img = Image.open(cStringIO.StringIO(file.read()))
            img.save('/tmp/%s' % name)
            self.thumbnail_url = File(open('/tmp/%s' % name))
            
            self.titre = obj.get("title", None)
        self.old_url = self.video        
        super(ContenuMedia, self).save(*args, **kwargs)   
       

moderator.register(Entry, EntryCommentModerator)
mptt.register(Category, order_insertion_by=['title'])
post_save.connect(ping_directories_handler, sender=Entry,
                  dispatch_uid='zinnia.entry.post_save.ping_directories')
post_save.connect(ping_external_urls_handler, sender=Entry,
                  dispatch_uid='zinnia.entry.post_save.ping_external_urls')
