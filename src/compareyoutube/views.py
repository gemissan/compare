from django.shortcuts import render, render_to_response

from django.contrib.auth.decorators import login_required

from compareobject.models import CompareObjectType
from compareyoutube.forms import AddYoutubeObjectForm


OBJECT_TYPE = CompareObjectType.objects.get(name="Youtube")


@login_required
def index(request):
    
    user = request.user
    repository = user.get_repository(OBJECT_TYPE).get_list_objects()
    if request.method == "POST":
        form = AddYoutubeObjectForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddYoutubeObjectForm()
    
    return render(request, "youtube_index.html", {"form": form, "repository": repository})


def list(request, username, list_name):
    
    return render_to_response("youtube_list.html")