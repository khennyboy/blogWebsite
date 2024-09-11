from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import *
import random

def index_view(request):
    posts = list(Post.objects.all())
    # random.shuffle(posts)  

    if request.method == "POST":
        next_url = request.POST.get('next', 'index') 
        page_id = request.POST.get('page_id', '') 
        category_post = request.POST.get('category', '')
    
        if not request.user.is_authenticated:
            return redirect('login')  

        post_id = request.POST.get('post_id')
     
        post = get_object_or_404(Post, id=post_id)
        
        try:
            existing_like = PostLike.objects.filter(user=request.user, eachpost=post)
            if existing_like.exists():
                post.likes = max(int(post.likes) - 1, 0)
                post.save()
                existing_like.delete()
                messages.success(request, f'You unliked {post.title}')
            else:
                post.likes = int(post.likes) + 1
                post.save()
                PostLike.objects.create(user=request.user, eachpost=post)
                messages.success(request, f'You liked {post.title}')
                
            if next_url == 'detailPost':
                next_url = f'post/{page_id}/'
            elif next_url == 'categoryPost':
                next_url = f'{category_post}/'
         
            return redirect(next_url)
        
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            if next_url == 'detailPost':
                next_url = f'post/{page_id}/'
            return redirect(next_url)

    if request.user.is_authenticated:
        post_likes = PostLike.objects.filter(user=request.user)
        liked_posts = {like.eachpost.id: True for like in post_likes}
        print(liked_posts)
    else:
        liked_posts = {}

    return render(request, 'index.html', {
        'all_post': posts,
        'liked_posts': liked_posts
    })

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('username')  
        password = request.POST.get('password')

        is_email = False
        try:
            validate_email(identifier)
            is_email = True
        except ValidationError:
            is_email = False

        if is_email:
            user = authenticate(request, email=identifier, password=password)
        else:
            user = authenticate(request, username=identifier, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')

@csrf_protect
def logout_view(request):
    logout(request)
    return redirect('index')

@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate email
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email address.")
            return render(request, 'signup.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'signup.html')

        # Create new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def category_view(request, category):
    posts = list(Post.objects.filter(categories__name=category))
    
    if request.user.is_authenticated:
        post_likes = PostLike.objects.filter(user=request.user)
        liked_posts = {like.eachpost.id: True for like in post_likes}
    else:
        liked_posts = {}
    return render(request, 'category.html', {
        'all_posts': posts,
        'category': category.capitalize(),
        "liked_post": liked_posts,
        'nameCategory': category,
    })


def details_view(request, id):
    post = Post.objects.get(pk = id)
    category = post.categories.name
    comments = Comment.objects.filter(post = post)
    print(comments)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, 'You need to be logged in to comment.')
            return redirect('login')  # Redirect to the login page

        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                post=post,
                user=request.user,
                content=content,
            )
            messages.success(request, 'Comment added!')
        else:
            messages.error(request, 'Comment cannot be empty.')

        return redirect('detailPost', id=post.id)
    
    other_posts = Post.objects.filter(categories__name=category).exclude(pk=id)
    if request.user.is_authenticated:
        post_likes = PostLike.objects.filter(user=request.user)
        liked_posts = {like.eachpost.id: True for like in post_likes}
    else:
        liked_posts = {}
    return render(request, 'details.html', {
        "post": post,
        "related_posts": other_posts,
        "liked_post": liked_posts,
        'comments': comments,
    })


