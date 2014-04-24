from django import forms

from compareyoutube.models import YoutubeObject


class AddObjectForm(forms.ModelForm):
    
    class Meta:
        model = YoutubeObject
