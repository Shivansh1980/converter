from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .ConverterTools import write_key, load_key, encryptFile, decryptFile
from .models import EncryptedFile
from converter import settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core.serializers import serialize
from .forms import EncryptedFileForm
from converter import settings

path_to_media = settings.MEDIA_ROOT
API_KEY = 1


# Create your views here.
def encrypthomepage(request):
    response_data = {'data': None, 'msg': None,  'downloadurl': None,'form':None}
    form = EncryptedFileForm()
    response_data['form'] = form
    return render(request, 'encryption/encryptionhome.html',response_data)

def decryptTheFile(requesst):
    response_data = {'data': None, 'msg': None, 'downloadurl': None}
    
def getEncryptionResult(request, file):
    fs = FileSystemStorage()
    filename = file.name
    path = path_to_media + filename

    fs.save(filename, file)
    write_key()
    k = load_key()
    encryptFile(path, k)
    downloadUrl = str(
        f"http://{request.META['REMOTE_ADDR']}:{request.META['SERVER_PORT']}/static/media/{filename}")
    result = {'downloadUrl': downloadUrl, 'key': k}

    return result


@csrf_exempt
def fileEncryptGetRequest(request):
    result = {'msg': '','error':None,'errors':'','url':None}
    if (request.method == "POST"):
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            file = request.FILES['file']
            encryptionResult = getEncryptionResult(request, file)

            encryptFile = EncryptedFile(
                useremail=request.POST['useremail'],
                key=encryptionResult['key'],
                url=encryptionResult['downloadUrl'],
                filename=file.name,
                file=file
            )

            result['msg'] = 'File Encryption Successfull'
            result['error'] = False
            result['url'] = encryptionResult['downloadUrl']
            print('url to download : ',result['url'])
            return JsonResponse(result)
        else:
            result['msg'] = "Wrong Input Provided"
            result['error'] = True
            result['errors'] = "Something Went Wrong"
            return JsonResponse(result)
    else:
        return JsonResponse({'msg':'Request Was Not POST'})

