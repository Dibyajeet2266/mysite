from django.contrib import admin
from django.urls import path
from blog import views

app_name ='blog'

urlpatterns = [
    path('',views.index,name='index'),
<<<<<<< HEAD
    path('post/',views.CreateView.as_view(),name='post_detail'),
    path('about/',views.AboutView.as_view(),name='about'),
=======
    path('post/',views.PostView.as_view(),name='post_detail'),
>>>>>>> frontend
]
