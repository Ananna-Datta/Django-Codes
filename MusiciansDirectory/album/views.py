from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def album(request):
    if request.method == 'POST':
        Album_form = forms.AlbumForm(request.POST)
        if Album_form.is_valid():
            Album_form.save()
            return redirect('album')
        
    else:
        Album_form = forms.AlbumForm()
    return render(request,'album.html', {'form':Album_form})

def edit_post(request,id):
    post = models.Album.objects.get(pk=id)
    post_form = forms.AlbumForm(instance=post)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.AlbumForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request,'homepage.html', {'form':post_form})


def delete_post(request,id):
    post = models.Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
