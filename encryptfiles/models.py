from django.db import models
from converter.settings import MEDIA_ROOT

# Create your models here.
class EncryptedFile(models.Model):
    file = models.FileField(upload_to=MEDIA_ROOT[1:]) #Starting from 1 because at begining /(slash) causeing problem but initial / works in linux
    useremail = models.EmailField(max_length=30)
    filename = models.CharField(max_length=20)
    key = models.CharField(max_length=300)
    url = models.CharField(max_length=100, null=True)
    

