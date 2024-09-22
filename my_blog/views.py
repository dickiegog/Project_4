from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.all()  # Retrieves all the posts from the Post model
    template_name = 'blog/post_list.html'  # Refers to the template file
