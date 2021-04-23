from django.db import models
from converter.settings import MEDIA_ROOT

# Create your models here.
class EncryptedFile(models.Model):
    username = models.CharField(max_length=40, null=True)
    my_file = models.FileField(upload_to=MEDIA_ROOT[1:]) #Starting from 1 because at begining /(slash) causing problem but initial / works in linux
    key = models.CharField(max_length=300, primary_key=True)
    url = models.CharField(max_length=100, null=True)
    

