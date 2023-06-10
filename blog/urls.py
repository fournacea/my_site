from django.urls import path

from . import views


urlpatterns = [
    path('', views.StartingPageView.as_view(), name="starting-page"), #/
    path('posts', views.AllPostsView.as_view(), name="posts-page"), #/posts
    path('posts/<slug:slug>', views.ViewPostDetail.as_view(), 
         name="post-detail-page"), #/posts/my-first-post
]
