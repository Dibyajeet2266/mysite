from django.contrib import admin
from django.urls import path
from blog import views

app_name ='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('post/',views.CreateView.as_view(),name='post_detail'),
    path('about/',views.AboutView.as_view(),name='about'),
]
