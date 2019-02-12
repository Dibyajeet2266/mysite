from django.contrib import admin
from django.urls import path
from blog import views

app_name ='blog'

urlpatterns = [
<<<<<<< HEAD
    path('',views.index,name='index'),
    path('new/',views.CreateView.as_view(),name='post_detail'),
    path('about/',views.AboutView.as_view(),name='about'),
<<<<<<< HEAD

=======
=======
    path('post/',views.PostView.as_view(),name='post_detail'),
>>>>>>> frontend
=======
    path('',views.PostListView.as_view(),name='post_list'),
    path('new/',views.CreateView.as_view(),name='post_view'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
>>>>>>> dj
>>>>>>> 971bfb9dcfc1d3ad44a2d3a24d902925c93a5008
]
