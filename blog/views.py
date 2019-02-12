from django.shortcuts import render
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm

from django.views.generic import TemplateView, DetailView,CreateView

class CreateView(CreateView):
    template_name = 'blog/form_detail.html'

def index(request):
    return render(request,'blog/index.html')

class CreateView(CreateView):
    template_name = 'blog/form_detail.html'
    form_class = PostForm

class login_page(TemplateView):
    template_name='blog/signin.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'
