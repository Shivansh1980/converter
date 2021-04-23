from django import forms
from .models import EncryptedFile
from converter import settings

class EncryptedFileForm(forms.ModelForm):
    class Meta:
        model = EncryptedFile
        fields =('my_file','username')

    
    