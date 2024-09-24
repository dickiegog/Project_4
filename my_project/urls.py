from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin path comes first to prevent slug match
    path('summernote/', include('django_summernote.urls')),  
    path('', include('my_blog.urls')),  # my_blog URLs come after admin and other fixed paths
]
