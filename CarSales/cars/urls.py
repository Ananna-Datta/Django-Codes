from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
    path('buy/<int:pk>/', views.ByeNow, name='buy'),
    
]