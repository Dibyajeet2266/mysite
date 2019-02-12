from django.shortcuts import render
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm

from django.views.generic import TemplateView,DetailView
# Create your views here.
# class AboutView(TemplateView):
#     template_name = 'blog/index.html'
#
#
# class PostFormView(FormView):
#      template_name = 'blog/form_detail.html'

def index(request):
    return render(request,'blog/index.html')

class PostView(FormView):
    template_name = 'blog/form_detail.html'
    form_class = PostForm
