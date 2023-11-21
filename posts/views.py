from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from . import models

def index(request):
    posts = models.Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

class Post(View):
    def get(self, request, pk):
        posts = models.Post.objects.get(id=pk)
        return render(request, 'posts/posts.html', {'posts': posts})
