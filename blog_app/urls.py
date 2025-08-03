from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("create/", views.create_post, name="create_post"),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]