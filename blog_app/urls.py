from django.urls import path

from blog_app import views

urlpatterns = [
    path("", views.index, name='index'),
    path("blog/<uuid:id>/", views.blog_detail_view, name='blog-detail'),
]
