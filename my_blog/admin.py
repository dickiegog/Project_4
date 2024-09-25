from django.contrib import admin
from .models import Post, Comment, About, CollaborateRequest 
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_on', 'read')
    list_filter = ('read', 'submitted_on')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)

# Register your models here.
admin.site.register(Comment)
