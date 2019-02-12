from django.contrib import admin
from django.urls import path
from blog import views

app_name ='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('post',views.PostView.as_view(),name='post_detail'),
]
