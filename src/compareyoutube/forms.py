from compareobject.forms import AddCompareObjectForm
from compareyoutube.models import YoutubeObject


class AddYoutubeObjectForm(AddCompareObjectForm):
    
    class Meta:
        model = YoutubeObject
        