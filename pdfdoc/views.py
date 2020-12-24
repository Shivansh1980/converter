from django.shortcuts import render
import pyrebase
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import os
import time
from docx2pdf import convert
from converter import settings
import pythoncom
import win32com.client
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
    params = {'status': '#'}
    for dirpath, dirnames, filenames in os.walk(settings.MEDIA_ROOT):
        for file in filenames:
            if (fnmatch(file, '*.pdf')):
                os.remove(os.path.join(dirpath, file))
    if request.method == 'POST':
        upload_file = request.FILES['word']
        fs = FileSystemStorage()
        fs.save(upload_file.name, upload_file)
        print('\n\nlocation is : ', fs.location)
        pythoncom.CoInitialize()
        filename = str(upload_file.name)
        print("FileName is : ",filename)
        path = settings.MEDIA_ROOT + filename
        print(path)

        #storage.child(path_on_cloud+f"/{filename}").put(path)


        dest = settings.MEDIA_ROOT+filename[0:-5]+'output.pdf'

        convert(path, dest)

        print("location : ", fs.location)
        params['status'] = True
        output = filename[0:-5] + 'output.pdf'
        os.remove(path)
        x = str(f"/static/media/{output}")
        params['url'] = x

    return render(request, "pdfanddoc/wordtopdf.html",params)
    
def providelink(request, id):
    if (request.method == 'GET'):
        return HttpResponse('true')
        
