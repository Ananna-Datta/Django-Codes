from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

# Create your views here.


class DetailPostView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object # post model er object ekhane store korlam
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


def ByeNow(request,pk):
    car = get_object_or_404(models.Car, pk=pk)
    car.quantity -= 1
    car.customer.add(request.user)
    # history = models.History(
    #     name=car.name,
    #     brand=car.brand,
    #     quantity=1,
    #     image = car.image,
    #     price=car.price,
    #     description = car.description,
    #     )
    # history.save()
    car.save()
    return redirect("profile")
    
    