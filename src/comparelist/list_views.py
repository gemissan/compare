import logging

from django.shortcuts import render_to_response


logger = logging.getLogger(__name__)


def repository(request):
    
    return render_to_response("repository.html")


def all_lists(request):
    
    return


def show_list(request, list_id):
    
    return


def create_list(request):
    
    return


def index(request):
    
    return
