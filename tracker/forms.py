from django import forms

from .models import CD

class CD_Form(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['band', 'album']
        labels = {"album": "Album", "band": "Band"}
