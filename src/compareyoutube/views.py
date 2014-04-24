import logging

from django.shortcuts import render
from django.views.generic import View

from compareyoutube.forms import AddObjectForm


logger = logging.getLogger(__name__)


class ShowListView(View):
    
    add_object_form = AddObjectForm
    template = "show_youtube_list.html"
    
    def get(self, request, *args, **kwargs):
        
        form = self.add_object_form()
        return render(request, self.template, {"form": form})
        
    def post(self, request, *args, **kwargs):
        
        form = self.form_class(request.POST)
        if form.is_valid():
            pass
        
        return render(request, self.template, {"form": form})

def create_list(request):
    
    return


def show_view(request):
    
    return


def create_view(request):
    
    return


def index(request):
    
    return
