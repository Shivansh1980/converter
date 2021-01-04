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

path_to_media = settings.MEDIA_ROOT
API_KEY = 1


# Create your views here.
def encrypthomepage(request):
    response_data = {'data': None, 'msg': None,  'downloadurl': None,'form':None}
    # if (request.method == "POST"):
    #     try:
    #         file = request.FILES['myfile']
    #         useremail = request.POST['email']
    #     except:
    #         response_data['msg'] = "File Not Exist Try Reuploading"
    #         return render('encryption/encryptionhome.html')

    #     fs = FileSystemStorage()
    #     fs.save(file.name, file)
    #     write_key()
    #     k = load_key()

    #     filename = file.name
    #     path = path_to_media+filename

    #     encryptFile(path, k)

    #     output = file.name
    #     # this is the url which we return as json response
    #     x = str(f"/static/media/{output}")

    #     encryptfile = EncryptedFile(
    #         useremail=useremail,
    #         filename=filename,
    #         key=k,
    #         file=file,
    #         url=x
    #     )
    #     encryptfile.save()

    #     print("File Path : "+fs.location)
    #     print("File Name : ", file.name)
    #     response_data['downloadurl'] = x
    #     response_data['msg'] = "Successfully Encrypted Your File"
    form = EncryptedFileForm()
    response_data['form'] = form
    return render(request, 'encryption/encryptionhome.html',response_data)

def decryptTheFile(requesst):
    response_data = {'data': None, 'msg': None, 'downloadurl': None}
    
    
@csrf_exempt
def fileEncryptGetRequest(request):
    result = {'msg': '','error':None,'errors':''}
    if (request.method == "POST"):
        print(request.POST)
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            result['msg'] = 'File Encryption Successfull'
            result['error'] = False
            return JsonResponse(result)
        else:
            result['msg'] = "Wrong Input Provided"
            result['error'] = True
            result['errors'] = form.errors
            return JsonResponse(result)
    else:
        return JsonResponse({'msg':'Request Was Not POST'})

