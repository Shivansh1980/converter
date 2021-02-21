from django import forms
from .models import EncryptedFile
from converter import settings

class EncryptedFileForm(forms.ModelForm):
    class Meta:
        model = EncryptedFile
        fields =('file','useremail')
class DecryptedFileForm(forms.Form):
    file = forms.FileField(upload_to=settings.MEDIA_ROOT[1:])
    key = forms.CharField(max_length=200)
    