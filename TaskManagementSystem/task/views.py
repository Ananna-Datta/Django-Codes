from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.taskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
        
    else:
        task_form = forms.taskForm()
    return render(request,'add_task.html', {'form':task_form})

def edit_post(request,id):
    post = models.Task.objects.get(pk=id)
    post_form = forms.taskForm(instance=post)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.taskForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request,'add_task.html', {'form':post_form})


def delete_post(request,id):
    post = models.Task.objects.get(pk=id)
    post.delete()
    return redirect('homepage')