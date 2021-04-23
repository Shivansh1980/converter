from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, FileResponse
from converter.ConverterTools import write_key, load_key, encrypt_file, decrypt_file, remove_file, get_correct_key
from .models import EncryptedFile
from .forms import EncryptedFileForm
from django.templatetags.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from converter import settings
from encryptfiles.serializers import EncryptedFileSerializer
from django.core import serializers

path_to_media = settings.MEDIA_ROOT
API_KEY = 1


# Create your views here.
def encrypt_homepage(request):
    response_data = {'data': None, 'msg': None,
                     'downloadurl': None, 'form': None}
    encryption_form = EncryptedFileForm()
    response_data['form'] = encryption_form
    return render(request, 'encryption/encryptionhome.html', response_data)

@csrf_exempt
def decrypt_file_request(request):
    if(request.method == 'POST'):
        try:
            key = get_correct_key(request.POST['key'])
            try:
                encrypted_file = EncryptedFile.objects.get(key=key)
                url = request.build_absolute_uri('/media/'+encrypted_file.my_file.name)
                if(encrypted_file.is_decrypted):
                    return JsonResponse({
                        'status':'error',
                        'error':True,
                        'error_msg':'This file already been decrypted cannot be decrypted again',
                        'url':url
                    })
                print('file name : ', encrypted_file.my_file.name)
                filepath = path_to_media + encrypted_file.my_file.name
                decrypt_file(filepath, key)
                encrypted_file.is_decrypted = True
                encrypted_file.save()
                return JsonResponse({
                    'msg':'file decrypted successfully',
                    'url': url,
                    'error': False,
                    'status': 'success'
                })

            except Exception as e:
                return JsonResponse({
                    'msg': 'File with this key does not exist on server',
                    'error': True,
                    'error_msg': str(e)
                })
        except Exception as e:
            return JsonResponse({
                'msg':'please post data with key to decrypt the file',
                'error':True,
                'error_msg':str(e)
            })


@csrf_exempt
def encrypt_file_request(request):
    if(request.method == 'POST'):
        form = EncryptedFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                my_file = request.FILES['my_file']
                write_key()
                k = load_key()

                k = get_correct_key(k)
                
                new_file = EncryptedFile(
                    username=form.cleaned_data['username'],
                    my_file=my_file,
                    key=k
                )
                new_file.save()

                #encrypting the file
                file_path = path_to_media + new_file.my_file.name
                encrypt_file(file_path,k)
                
                url = request.build_absolute_uri('/media/'+new_file.my_file.name)

                return JsonResponse({
                    'key':k,
                    'url':url,
                    'error':False,
                    'status':'success'
                })

            except Exception as e:
                return JsonResponse({
                    'status':'Internal Server Error',
                    'msg':str(e),
                    'error':True,
                    'error_msg':str(e)          
                })
        else:
            return JsonResponse({
                'status':'error',
                'error': True, 
                'error_msg':form.errors
                })

@csrf_exempt
def delete_all_files(request):
    if(request.method == 'DELETE'):
        files = EncryptedFile.objects.all()
        for f in files:
            f.my_file.delete()
            f.delete()
        return JsonResponse({
            'status': 'success',
            'msg':'all files has been deleted',
            'error':False
        })
    else:
        return JsonResponse({'error_msg': 'please  make delete request for deleting a file', 'error': True})

@csrf_exempt
def delete_file(request, key):
    key = get_correct_key(key)
    if(request.method == 'DELETE'):
        try:
            encrypted_file = EncryptedFile.objects.get(key=key)
            encrypted_file.delete()
            return JsonResponse({'msg':'file deleted successfully', 'error':False})
        except Exception as e:
            return JsonResponse({
                'error':True,
                'error_msg': 'file not exists on server'
            })
    else:
        return JsonResponse({ 
            'error': True,
            'error_msg': 'please  make delete request for deleting a file'
        })

@csrf_exempt
def is_file_exists(request, key):
    key = get_correct_key(key)
    if(request.method == 'GET'):
        try:
            encrypted_file = EncryptedFile.objects.get(key=key)
            return JsonResponse({'status': 'success',  'msg': 'file exists on server', 'error': False, 'is_exist': True})
        except Exception as e:
            return JsonResponse({'status': 'success',  'msg': 'file does on exists on server', 'error': False, 'is_exist': False})
    else:
        return JsonResponse({'status':'error', 'error_msg': 'please make get request for it', 'error': True})
