from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

from blog_app.models import Post

# Create your views here.

def index(request):
    all_posts = Post.objects.all()
    if not request.user.is_authenticated:
        all_posts = Post.objects.all()[:3]
        
    # return HttpResponse("Hello World",)
    return render(request, 'blog_app/index.html', {'all_posts':all_posts})


# @login_required()
def blog_detail_view(request, id):
    post = Post.objects.get(post_id=id)
    
    # return HttpResponse("Blog Detail View")
    return render(request, 'blog_app/blog_detail.html', {'post':post,},)


