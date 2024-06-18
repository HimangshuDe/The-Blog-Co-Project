from django import forms

from blog_app.models import Post

class AddBlogPost(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ['created_at', 'updated_at', 'creator']