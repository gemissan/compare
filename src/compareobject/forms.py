from django import forms

from compareobject.models import CompareObject


class AddCompareObjectForm(forms.ModelForm):
    
    class Meta:
        model = CompareObject