from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

from auth_app.models import UserModel
from blog_app.forms import AddBlogPost
from blog_app.models import Post

# Create your views here.

def index(request):
    return render(request, 'blog_app/index.html')

def all_blogs(request):
    request.session['blog_detail'] = False
    all_posts = Post.objects.all()
    if not request.user.is_authenticated:
        all_posts = Post.objects.all()[:3]
    
        
    # return HttpResponse("Hello World",)
    return render(request, 'blog_app/all_blogs.html', {'all_posts':all_posts})


def blog_detail_view(request, id):
    post = Post.objects.get(post_id=id)
    request.session['blog_detail'] = True

    return render(request, 'blog_app/blog_detail.html', {'post':post,},)


@login_required
def create_blog(request):
    form = AddBlogPost()
    if request.method == 'POST':
        form = AddBlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.save()
            return redirect('index')
        
        return render(request, "blog_app/add_blog_post.html", {'form':form})
        
    return render(request, "blog_app/add_blog_post.html", {'form':form})
# :: Note Section ::
# NOTE #1: Add "Add blog" feature in the project
# NOTE #2: Implement addition of new tags via "add blog" feature, whenever user enters a new tag in
# the tag field if it exists then no change, if not, then a new tag will be created from 
# the entered tag.