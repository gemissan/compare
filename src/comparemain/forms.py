from django import forms

from django.contrib.auth import get_user_model


User = get_user_model()


class UsernameField(forms.TextInput):
    
    class Media:
        css = {
            "all": ("css/forms.css",)
        }


class EmailField(forms.TextInput):
    
    class Media:
        css = {
            "all": ("css/forms.css",)
        }
        
        
class PasswordField(forms.PasswordInput):
    
    class Media:
        css = {
            "all": ("css/forms.css",)
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=UsernameField(attrs={"class": "login_input"}))
    password = forms.CharField(widget=PasswordField(attrs={"class": "login_input password_input"}))
        
    class Media:
        css = {
            "all": ("css/forms.css", "css/login.css",)
        }
