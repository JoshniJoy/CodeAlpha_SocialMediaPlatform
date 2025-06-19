from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Core
    path('', views.feed_view, name='feed'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),

    # Posts and Comments
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    
    # ADD THIS LINE FOR THE SEARCH URL
    path('search/', views.search_view, name='search'),

    # API-like endpoints for JS
    path('toggle_follow/<str:username>/', views.toggle_follow, name='toggle_follow'),
    path('toggle_like/<int:post_id>/', views.toggle_like, name='toggle_like'),
]