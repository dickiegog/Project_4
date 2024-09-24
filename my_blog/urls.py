from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about_me, name='about'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
