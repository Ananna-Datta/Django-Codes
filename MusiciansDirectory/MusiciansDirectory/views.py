
from django.shortcuts import render
from album.models import Album
from album.models import Musician

def home(request):
    data=Album.objects.select_related('musician').all()
    return render(request, 'home.html', {'data': data })


