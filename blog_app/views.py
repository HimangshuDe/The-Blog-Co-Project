from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

from blog_app.forms import AddBlogPost
from blog_app.models import Post, Tag

# Create your views here.

def index(request):
    all_posts = Post.objects.all()
    all_tags = Tag.objects.all()
    if not request.user.is_authenticated:
        all_posts = Post.objects.all()[:3]
        
    # return HttpResponse("Hello World",)
    return render(request, 'blog_app/index.html', {'all_posts':all_posts, 'all_tags':all_tags})


# @login_required()
def blog_detail_view(request, id):
    post = Post.objects.get(post_id=id)
    
    # return HttpResponse("Blog Detail View")
    return render(request, 'blog_app/blog_detail.html', {'post':post,},)


def create_blog(request):
    form = AddBlogPost()
    return render(request, "blog_app/add_blog_post.html", {'form':form})
# :: Note Section ::
# NOTE #1: Add "Add blog" feature in the project
# NOTE #2: Implement addition of new tags via "add blog" feature, whenever user enters a new tag in
# the tag field if it exists then no change, if not, then a new tag will be created from 
# the entered tag.