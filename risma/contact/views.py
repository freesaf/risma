# -*- coding: utf-8 -*- 
from annoying.decorators import render_to
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from forms import ContactForm

@render_to("contact/contact.html")
def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Formulaire envoyé avec succès.'))
            return HttpResponseRedirect(reverse("contact-confirmation-envoi"))
    else:
         form = ContactForm()
    return {"form": form}