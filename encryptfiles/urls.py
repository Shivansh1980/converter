from django.urls import path, include
from .views import encrypthomepage, encryptFileRequest, decryptFileRequest
urlpatterns = [
    path('', encrypthomepage, name='encryptfilehomepage'),
    #path('file-encrypt/', encrypthomepage, name='encryptfile')
    path('file-encrypt/', encryptFileRequest, name='encryptfile'),
    path('file-decrypt/', decryptFileRequest, name='decryptfile')
]
