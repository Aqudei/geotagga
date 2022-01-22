import imp
from django import forms

class UploadForm(forms.Form):
    excel = forms.FileField()
    file = forms.FileField()