from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/list.html', context)

def create(request):
    form = PostForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/list')
    context = {'form': form} 
    return render(request, 'post/create.html', context)
