from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .ConverterTools import write_key, load_key, encryptFile, decryptFile
from .models import EncryptedFile
from converter import settings


path_to_media = settings.MEDIA_ROOT

# Create your views here.
def encrypthomepage(request):
    param = {'file': ''}
    username = ""
    if (request.method == "POST"):
        try:
            file = request.FILES['myfile']
            useremail = request['email']

        except:
            return render(request, 'encryption/encryptionhome.html', param)
        fs = FileSystemStorage()
        write_key()
        k = load_key()
        filename = file.name
        path = path_to_media+"outputs\\"+filename
        print("Destination Path : ", path)
        
        output = file.name
        x = str(f"/static/media/outputs/{output}")
        encryptFile()
        encryptfile = EncryptedFile(
            useremail = username,
            filename=filename,
            key=k,
            file=file,
            url=x
        )
        encryptfile.save()

        print("File Path : "+fs.location)
        print("File Name : ",file.name)
        param['file'] = x
        print(param['file'])
        return render(request, 'encryption/encryptionhome.html', param)
    return render(request, 'encryption/encryptionhome.html', param)
