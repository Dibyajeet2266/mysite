from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm
from django.utils import timezone

from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView

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
