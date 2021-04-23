from django.shortcuts import render
import pyrebase
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import time
from converter.ConverterTools import DocxToPdf , remove_files
from converter import settings
import threading
import time
from fnmatch import fnmatch

path_on_cloud = "images"
path_on_local = settings.MEDIA_ROOT

def pdfdochome(request):
    return render(request,'pdfanddoc/pdfdoc.html')

def pdftodoc(request):
    params = {'status': False}
    if (request.method == 'POST'):
        upload_file = request.FILES['pdf']
        print('filename : ',upload_file.name)
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        return JsonResponse(params)

    return render(request, "pdfanddoc/pdftoword.html",params)


def doctopdf(request):

    res = {'status':False}
    print(request.build_absolute_uri())
    print(request.get_host())
    
    if request.method == 'POST':
        upload_file = request.FILES['word']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        print('\n\nlocation is : ', fs.location)

        res = DocxToPdf(request, "/static/media")
        print("Your Result : ",res)
        print("You File Path : ",res)

    return render(request, "pdfanddoc/wordtopdf.html", res)
    
def providelink(request, id):
    if (request.method == 'GET'):
        return HttpResponse('true')
        
