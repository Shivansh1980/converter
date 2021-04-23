from django.urls import path, include
from .views import encrypt_homepage, encrypt_file_request, delete_all_files, delete_file, is_file_exists, decrypt_file_request
urlpatterns = [
    path('', encrypt_homepage, name='encryptfilehomepage'),
    path('encrypt_file/', encrypt_file_request, name='encryptfile'),
    path('decrypt_file/', decrypt_file_request, name='decryptfile'),
    path('delete_all_files/',delete_all_files, name='deletefiles'),
    path('is_file_exists/<str:key>', is_file_exists, name='isfileexists'),
    path('delete_file/<str:key>', delete_file, name='deletefile')
]
