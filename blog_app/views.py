from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/index.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Successfully registered!")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('login')

@ login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog_app/create_post.html', {'form': form})

@ login_required
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponse("Unauthorized", status=401)
    
    if request.method=="POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/update_post.html', {'form': form})

@ login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponse("Unauthorized", status=401)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect('index')

    return render(request, 'blog_app/delete_post.html', {'post': post})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog_app/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })