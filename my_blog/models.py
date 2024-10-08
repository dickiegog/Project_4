from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

CATEGORY_CHOICES = [
    ('tech', 'Tech'),
    ('lifestyle', 'Lifestyle'),
    ('education', 'Education'),
    ('sports', 'Sports'),
]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Post Model

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True, null=True)  
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True) 
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='tech')
    status = models.CharField(max_length=10, choices=(('Draft', 'Draft'), ('Published', 'Published')), default='Draft')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.post} by {self.author}"

# About model
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
        
#  Collaboration Requests
class CollaborateRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)  # To mark requests as read
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
