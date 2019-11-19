from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

posts = [
    {
        'author': 'Khang',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 27, 2019'
    },
    {
        'author': 'Nhat Ha',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Home'
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
