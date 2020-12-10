from django import forms
class FileInput(forms.Form):
    pdf = forms.FileField(upload_to='pdf/')