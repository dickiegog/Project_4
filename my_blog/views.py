from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q 
from .models import Post, About, CollaborateRequest, Comment, Category, CATEGORY_CHOICES
from .forms import CommentForm, CollaborateForm

class PostList(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 6

    def get_queryset(self):
        # Start with all posts
        queryset = Post.objects.all()

        # Handle search query
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )

        # Handle category filter
        category_filter = self.request.GET.get('category')
        if category_filter and category_filter != 'All Categories':
            queryset = queryset.filter(Q(category=category_filter) | Q(category=''))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch categories from CATEGORY_CHOICES and add "All Categories" option
        context['categories'] = ['All Categories'] + [category[0] for category in CATEGORY_CHOICES]

        # Preserve query and selected category in the context
        context['query'] = self.request.GET.get('q') or ''
        context['selected_category'] = self.request.GET.get('category') or ''
        
        return context

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )

def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Collaboration request received! Thank you I will respond as soon as possible."
            )
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "blog/about.html", 
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )
def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        queryset = Post.objects.filter(status='Published')
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    View to delete comment
    """
    post = get_object_or_404(Post, slug=slug, status='Published')  # Ensure this matches
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status='Published')
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
