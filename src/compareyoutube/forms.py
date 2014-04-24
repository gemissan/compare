from django import forms

from compareyoutube.models import YoutubeObject


class YoutubeUrlField(forms.forms.TextInput):
    
    class Media:
        css = {
            "all": ("css/forms.css", "css/youtube.css",)
        }


class AddObjectForm(forms.Form):
    
    url = forms.CharField(widget=YoutubeUrlField(attrs={"class": "url_input youtube_url_input"}))
        
    class Media:
        css = {
            "all": ("css/forms.css", "css/youtube.css",)
        }
