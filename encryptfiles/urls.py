from django.urls import path, include
from .views import encrypthomepage, fileEncryptGetRequest
urlpatterns = [
    path('', encrypthomepage, name='encryptfilehomepage'),
    #path('file-encrypt/', encrypthomepage, name='encryptfile')
    path('file-encrypt/', fileEncryptGetRequest, name='encryptfile')
]
