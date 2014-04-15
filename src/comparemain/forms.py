from django import forms

from django.contrib.auth import get_user_model


User = get_user_model()


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


class LoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            "email": EmailField(attrs={"class": "login_input"}),
            "password": PasswordField(attrs={"class": "login_input password_input"})
        }
        
    class Media:
        css = {
            "all": ("css/forms.css",)
        }
