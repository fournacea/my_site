from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView



from .models import Post
from .forms import CommentForm


# def get_date(post):
#     return post["date"]

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data
    

# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, 'blog/index.html', {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, 'blog/all-posts.html', {
#         "all_posts": all_posts
#     })


class ViewPostDetail(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = CommentForm()
        return context


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post-detail.html', {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })

# def post_detail(request, slug):
#     # all_posts = Post.objects.all()
#     try:
#         identified_post = next(post for post in all_posts if post["slug"] == slug)
#     except StopIteration:
#         # Handle the case when the post is not found
#         return render(request, 'blog/post-not-found.html')
    
#     return render(request, 'blog/post-detail.html', {
#         "post": identified_post
#     })