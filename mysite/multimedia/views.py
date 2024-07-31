from django.shortcuts import render

from .models import Media

def index(request):
    media_items = Media.objects.all()
    return render(request, 'multimedia/index.html', {'media_items': media_items})
