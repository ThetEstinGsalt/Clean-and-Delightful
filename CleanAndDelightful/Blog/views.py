from django.shortcuts import render, HttpResponse
from .models import Blog
# Create your views here.


def blog(request, sno):
    # blogs = Post.objects.all()

    blog = Blog.objects.filter(auto_increment_id=sno)

    # if(sno == len(blogs)):
    #     next_blog = int(sno)-int(sno-1)
    #     prev_blog = int(sno)-1
    #     blog_next = Post.objects.filter(auto_increment_id=next_blog)
    #     blog_prev = Post.objects.filter(auto_increment_id=prev_blog)

    # elif(sno == 1):
    #     prev_blog = len(blogs)
    #     next_blog = int(sno)+1
    #     blog_next = Post.objects.filter(auto_increment_id=next_blog)
    #     blog_prev = Post.objects.filter(auto_increment_id=prev_blog)

    # else:
    #     prev_blog = int(sno)-1
    #     next_blog = int(sno)+1
    #     blog_next = Post.objects.filter(auto_increment_id=next_blog)
    #     blog_prev = Post.objects.filter(auto_increment_id=prev_blog)
    # , {'blog': blog[0]}
    return render(request, 'blog.html', {'blog': blog[0]})
