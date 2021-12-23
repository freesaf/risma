#-*- coding: utf-8 -*-
import os
import mimetypes

from django.contrib.auth.decorators import login_required
from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from models import Fichier


@login_required
def download(request, file_id):
    """Retourne un fichier partie de la base de données"""
    file = get_object_or_404(Fichier, id=file_id)
    path = file.fichier.path
    fsock = FileWrapper(open(path))                                                                                                        
    content_type, encoding = mimetypes.guess_type(path)                                                                          
    
    response = HttpResponse(fsock, content_type = content_type)                                                                    
    response['Content-Length'] = os.path.getsize(path)                                                  
    response['Content-Encoding'] = encoding                                                                                        
    response['Content-Disposition'] = 'attachment; filename=%s' % str(file).split('/')[-1]
    return response