from django.db import models
from converter.settings import MEDIA_ROOT
from .storage import OverwriteStorage
# Create your models here.
class EncryptedFile(models.Model):
    file = models.FileField(upload_to=MEDIA_ROOT)
    useremail = models.EmailField(max_length=30)
    filename = models.CharField(max_length=20)
    key = models.CharField(max_length=300)
    url = models.CharField(max_length=100, null=True)
    

