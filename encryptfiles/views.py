from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from .ConverterTools import write_key, load_key, encryptFile, decryptFile, removeFiles
from .models import EncryptedFile
from converter import settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.core.serializers import serialize
from .forms import EncryptedFileForm, DecryptedFileForm
from converter import settings
from django.templatetags.static import static

import glob

path_to_media = settings.MEDIA_ROOT
API_KEY = 1


# Create your views here.
def encrypthomepage(request):
    response_data = {'data': None, 'msg': None,  'downloadurl': None,'form':None}
    encryption_form = EncryptedFileForm()
    decryption_form = DecryptedFileForm()
    response_data['form'] = encryption_form
    response_data['decryption_form'] = decryption_form
    return render(request, 'encryption/encryptionhome.html',response_data)

def getDecryptFileResult(request, file):
    fs = FileSystemStorage()
    filename = file.name
    path = path_to_media + filename
    fs.save(filename, file)
    key = request.POST['key']
    decryptFile(path, key)
    print('path for decryption : ', path)
    url = str(f"http://{request.META['REMOTE_ADDR']}:{request.META['SERVER_PORT']}/static/media/{filename}")
    return {'msg': 'decryption success', 'url': url}
    
@csrf_exempt
def decryptFileRequest(request):
    response_data = None
    if (request.method == "POST"):
        form = DecryptedFileForm(request.POST, request.FILES)
        if(form.is_valid()):
            file = request.FILES['file']
            print("file structure : ", file)
            path = settings.MEDIA_ROOT + file.name
            response_data = getDecryptFileResult(request, file)
            response_data['error'] = None
            response_data['errors'] = None
            return JsonResponse(response_data)
        else :
            response_data['error'] = 'Please Provide Valid Input'
            response_data['errors'] = 'Something Went Wrong On Your Side'
            return response_data     

def getEncryptionResult(request, file):
    fs = FileSystemStorage()
    filename = file.name
    path = path_to_media + filename

    fs.save(filename, file)
    print('file saved to ', fs.location)
    write_key()
    k = load_key()
    encryptFile(path, k)
    
    downloadUrl = static('media\\'+str(file.name))
    k = str(k)
    result = {'downloadUrl': downloadUrl, 'key': k, 'path':path}
    return result


@csrf_exempt
def encryptFileRequest(request):
    result = {'msg': '','error':None,'errors':'','url':None,'key':None}
    if (request.method == "POST"):
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print('file structure : ', file)
            path = settings.MEDIA_ROOT + file.name
            print(path)
            encryptionResult = getEncryptionResult(request, file)
            encryptFile = EncryptedFile(
                useremail=request.POST['useremail'],
                key=encryptionResult['key'],
                url=encryptionResult['downloadUrl'],
                path=encryptionResult['path'],
            )
            encryptFile.save()

            result['msg'] = 'File Encryption Successfull'
            result['error'] = False
            result['url'] = encryptionResult['downloadUrl']
            result['key'] = encryptionResult['key']
            print('url to download : ',result['url'])
            return JsonResponse(result)
        else:
            result['msg'] = "Wrong Input Provided"
            result['error'] = True
            result['errors'] = "Something Went Wrong"
            return JsonResponse(result)
    else:
        return JsonResponse({'msg': 'Request Was Not POST'})
        
