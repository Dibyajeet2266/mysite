<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render,get_object_or_404,redirect
>>>>>>> ccb73e74ff9ea261abe1c6fd0f5aed2772d9f441
from blog.models import Post
from django.views.generic.edit import FormView
from blog.forms import PostForm,CommentForm,UserCreateForm
from . import forms
from django.utils import timezone
<<<<<<< HEAD
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView


=======
from django.urls import reverse_lazy,reverse
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView
# Create your views here.
# class AboutView(TemplateView):
#     template_name = 'blog/index.html'
#
#
# class PostFormView(FormView):
#      template_name = 'blog/form_detail.html'
>>>>>>> ccb73e74ff9ea261abe1c6fd0f5aed2772d9f441
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'

<<<<<<< HEAD
=======

>>>>>>> ccb73e74ff9ea261abe1c6fd0f5aed2772d9f441
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
<<<<<<< HEAD
    """
    Accept and reject buttons required depending upon the authorization
    if authorized:
        if reviewers:
            show buttons
        else:
            dont show buttons
    """

class PostReviewerListView(ListView):
    """
        Returns the pending Post for each reviewer
    """
    template_name = 'blog/-------'
    model  = Post

    # def get_queryset(self):
    #     """
    #     Gets the id of the reviewer and returns the pending ads
    #     """
    #     if reviewer 1 :
    #         return Post.objects.filter(rev1_status__exact=0).order_by('start_date')
    #     elif reviewer 2:
    #         return Post.objects.filter(rev2_status__exact=0).order_by('start_date')
    #     else:
    #         return Post.objects.filter(rev3_status__exact=0).order_by('start_date')
=======

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
>>>>>>> ccb73e74ff9ea261abe1c6fd0f5aed2772d9f441
