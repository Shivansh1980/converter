from django.urls import path, include
from .views import encrypthomepage
urlpatterns = [
    path('', encrypthomepage, name='encryptfilehomepage'),
    path('file-encrypt',encrypthomepage, name='encryptfile')
]
