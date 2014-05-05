import logging

from django.shortcuts import render
from django.views.generic import View

from compareyoutube.forms import AddObjectForm
from compareobject.models import CompareObjectType
from compareyoutube.models import YoutubeObject


logger = logging.getLogger(__name__)


youtube_type = CompareObjectType.objects.get(slug="youtube")
    

class ShowListView(View):
    
    add_object_form = lambda self: AddObjectForm(prefix="add-youtube")
    template = "show_youtube_list.html"
    
    def _get_objects(self, request):
        
        return []
    
    def get(self, request, *args, **kwargs):
        
        form = self.add_object_form()
        return render(request, self.template, {"form": form, "objects": self._get_objects(request)})
        
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
        
        return render(request, self.template, {"form": form, "objects": self._get_objects(request)})
    
    

class ShowRepositoryView(ShowListView):
    
    def _get_objects(self, request):
        
        return YoutubeObject.objects.filter(pk__in=request.user.get_repository(youtube_type).list_objects.all())

def create_list(request):
    
    return


def show_view(request):
    
    return


def create_view(request):
    
    return


def index(request):
    
    return
