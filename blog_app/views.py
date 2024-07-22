from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
# from django.http import HttpResponse

from auth_app.models import UserModel
from blog_app.forms import AddBlogPost
from blog_app.models import Post

# Create your views here.

def index(request):
    return render(request, 'blog_app/index.html')

def all_blogs(request):
    request.session['off_home'] = False
    all_posts = Post.objects.all()
    if not request.user.is_authenticated:
        all_posts = Post.objects.all()[:3]
    
        
    # return HttpResponse("Hello World",)
    return render(request, 'blog_app/all_blogs.html', {'all_posts':all_posts})


def blog_detail_view(request, id):
    post = Post.objects.get(post_id=id)
    request.session['off_home'] = True

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


@login_required
def list_user_blogs(request):
    user = request.user
    request.session['off_home']=True
    user_blog_posts = Post.objects.filter(creator=user)
    return render(request, 'blog_app/user_blogs.html', {'blogs':user_blog_posts})
    
