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

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts/list')
    context = {'form': form}
    return render(request, 'post/create.html', context)

def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/posts/list')

    context = {'post': post}
    return render(request, 'post/delete.html', context)
