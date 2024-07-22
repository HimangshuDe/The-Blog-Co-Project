from django.urls import path

from blog_app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("blog/all", views.all_blogs, name='all-blogs'),
    path("blog/<uuid:id>/", views.blog_detail_view, name='blog-detail'),
    path('blog/add/', views.create_blog, name='add-blog'),
    path('blog/list/user-posts/', views.list_user_blogs, name='user-blogs')
]
