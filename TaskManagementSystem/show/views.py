from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def show_post(request):
    if request.method == 'POST':
        show_form = forms.showForm(request.POST)
        if show_form.is_valid():
            show_form.save()
            return redirect('show_post')
        
    else:
        show_form = forms.showForm()
    return render(request,'post.html', {'form':show_form})


def edit_post(request,id):
    show = models.Show.objects.get(pk=id)
    show_form = forms.showForm(instance=show)
    # print(post.title)
    if request.method == 'POST':
        show_form = forms.showForm(request.POST, instance=show)
        if show_form.is_valid():
            show_form.save()
            return redirect('show_post')
    return render(request,'post.html', {'form':show_form})

def delete_post(request,id):
    post = models.Show.objects.get(pk=id)
    post.delete()
    return redirect('show_post')
