from django import forms

from .models import CD

class CD_Form(forms.ModelForm):
    class Meta:
        model = CD
        fields = ['band', 'album', 'other',]
        labels = {"album": "Album", "band": "Band", 'other': 'Other', 'groups': 'Groups'} 
        widgets = {
            'other': forms.Textarea(attrs={'rows': 2, 'cols': 25}),
        }

