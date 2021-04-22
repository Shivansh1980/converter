from django import forms
from .models import EncryptedFile, DecryptedFile
from converter import settings

class EncryptedFileForm(forms.ModelForm):
    class Meta:
        model = EncryptedFile
        fields =('file','useremail')
class DecryptedFileForm(forms.ModelForm):
    class Meta:
        model = DecryptedFile
        fields = '__all__'
    
    