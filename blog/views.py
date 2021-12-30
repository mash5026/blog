from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Post
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# from django.urls import reverse, reverse_lazy

# Create your views here.

def home(request):
    return render(request, 'home.html')
    # return redirect('blog:all_post', slug="hello", id=2)
    # return HttpResponseRedirect(reverse('blog:all_post', kwargs={"slug":"slug"}))

def all_post(request):
    posts = Post.objects.all()
    context ={
        "posts":posts
    }
    return render(request, 'blog/all_posts.html', context)

@login_required
def details(request,slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(status=0)
    context = {
        'post':post,
        'comments':comments,
    }
    return render(request,'blog/detils.html', context)
    