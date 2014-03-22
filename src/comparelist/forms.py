from django import forms

from comparelist.models import CompareList, CompareFeature
from compareobject.models import CompareObject, CompareCategory, CompareObjectType
        

class CreateNewListForm(forms.ModelForm):
    """
    """
    
    class Meta:
        model = CompareList
        fields = ["name", "object_type", "categories", "features", "list_objects"]
        
    name = forms.CharField()
    object_type = forms.ModelChoiceField(queryset=CompareObjectType.objects.all())
    categories = forms.ModelMultipleChoiceField(queryset=CompareCategory.objects.all())
    features = forms.ModelMultipleChoiceField(queryset=CompareFeature.objects.all())
    list_objects = forms.ModelMultipleChoiceField(queryset=CompareObject.objects.all())
    
        