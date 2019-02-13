from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm
from . import forms
from django.utils import timezone
<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView,CreateView,ListView
# Create your views here.
# class AboutView(TemplateView):
#     template_name = 'blog/index.html'
#
#
# class PostFormView(FormView):
#      template_name = 'blog/form_detail.html'
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'


=======

from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView
>>>>>>> 428e05ae3007acfed02d9bfe4f970b0669c7e784

def index(request):
    return render(request,'blog/index.html')

class CreateView(CreateView):
    template_name = 'blog/form_detail.html'
    form_class = PostForm

class PostUpdateView(UpdateView):
      template_name = 'blog/form_update.html'
      model = Post
      form_class = PostForm
      exclude =  ['rev1_status', 'rev2_status', 'rev3_status']
      success_url = '/'

class login_page(TemplateView):
    template_name='blog/signin.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    template_name ='blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(start_date__lte=timezone.now()).order_by('-start_date')

class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    queryset = Post.objects.all()
