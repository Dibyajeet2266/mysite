from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

app_name ='blog'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="blog/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(template_name="blog/signup.html"),name='signup'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('new/',views.CreateView.as_view(),name='post_view'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'post_update'),
    path('ppost/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),

]
