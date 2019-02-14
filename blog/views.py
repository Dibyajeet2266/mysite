from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm,CommentForm,UserCreateForm
from . import forms
from django.utils import timezone
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView
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

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
