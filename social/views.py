from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment, Follow, Profile
from .forms import PostForm, CommentForm, ProfileForm
from django.http import JsonResponse
from django.contrib import messages

# --- Authentication Views ---

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('feed')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('feed')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'social/signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('feed')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f"Welcome back, {user.username}!")
            return redirect('feed')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'social/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request, "You have been successfully logged out.")
        return redirect('login')

# --- Core App Views ---

@login_required
def feed_view(request):
    following_ids = request.user.following.values_list('followed_id', flat=True)
    user_and_following_ids = list(following_ids) + [request.user.id]
    posts = Post.objects.filter(author_id__in=user_and_following_ids)
    post_form = PostForm()
    return render(request, 'social/feed.html', {'posts': posts, 'post_form': post_form})

@login_required
def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=profile_user)
    is_following = Follow.objects.filter(follower=request.user, followed=profile_user).exists()
    is_own_profile = (request.user == profile_user)
    return render(request, 'social/profile.html', {
        'profile_user': profile_user,
        'posts': posts,
        'is_following': is_following,
        'is_own_profile': is_own_profile
    })

@login_required
def edit_profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'social/edit_profile.html', {'form': form})

# --- Post and Comment Views ---

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Your post has been created!")
        else:
            messages.error(request, "There was an error creating your post. Please check the form.")
    return redirect('feed')

@login_required
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentForm()
    comments = post.comments.all() 
    return render(request, 'social/post_detail.html', {'post': post, 'comment_form': comment_form, 'comments': comments})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
    return redirect('post_detail', post_id=post.id)

# --- Search View ---

@login_required
def search_view(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = User.objects.filter(username__icontains=query)
        
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'social/search_results.html', context)


# --- Follow/Like Logic (for JS) ---

@login_required
def toggle_follow(request, username):
    if request.method == 'POST':
        user_to_follow = get_object_or_404(User, username=username)
        if user_to_follow == request.user:
            return JsonResponse({'error': "You cannot follow yourself."}, status=400)

        follow, created = Follow.objects.get_or_create(follower=request.user, followed=user_to_follow)
        
        if not created: 
            follow.delete()
            is_following = False
        else:
            is_following = True
            
        return JsonResponse({'is_following': is_following})
    return redirect('profile', username=username)

@login_required
def toggle_like(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True
        
        return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})
    return redirect('feed')