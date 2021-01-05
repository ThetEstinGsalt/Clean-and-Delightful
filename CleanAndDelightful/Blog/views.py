from django.shortcuts import render, HttpResponse

# Create your views here.


def blog(request, post):
    return render(request, 'blog.html')
