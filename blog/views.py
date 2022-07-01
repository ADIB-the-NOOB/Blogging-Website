from django.shortcuts import render
from .models import Post, Comment
# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'blog/home.html',context)
