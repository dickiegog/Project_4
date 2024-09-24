from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, About

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status='Published')
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

def about_me(request):
    """
    Fetch and display the 'About' content.
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "blog/about.html",  # Remove "my_blog"
        {"about": about},
    )
