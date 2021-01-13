from django.shortcuts import render
import pyrebase
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import time
from encryptfiles.ConverterTools import DocxToPdf , removeFiles
from converter import settings
import threading
import time
from fnmatch import fnmatch

config = {
    'apiKey': "AIzaSyBwRxD6o8eC5FNDBIpW0wmawafM13pCXho",
    'authDomain': "converter-b30ab.firebaseapp.com",
    'projectId': "converter-b30ab",
    'databaseURL':"https://converter-b30ab.firebaseio.com",
    'storageBucket': "converter-b30ab.appspot.com",
    'messagingSenderId': "850133980369",
    'appId': "1:850133980369:web:531c1148c41b0db30ae1f0",
    'measurementId': "G-YQ3YVHVQYR"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

storage = firebase.storage()
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
    if request.method == 'POST':
        removeFiles(".docx")
        upload_file = request.FILES['word']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        print('\n\nlocation is : ', fs.location)

        res = DocxToPdf("/static/media")
        #storage.child(path_on_cloud+f"/{filename}").put(path)

    return render(request, "pdfanddoc/wordtopdf.html", res)
    
def providelink(request, id):
    if (request.method == 'GET'):
        return HttpResponse('true')
        
