from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginForm(forms.Form):
    """
    """

    name = forms.CharField(max_length=50)
    
    
class CreateUserForm(forms.ModelForm):
    """
    """
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]
    
    confirm_password = forms.PasswordInput()
