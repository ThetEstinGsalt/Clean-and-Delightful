from django.shortcuts import render, HttpResponse
from .models import Contact, cardimage, contacts, about, social
from Blog.models import Blog
from django.core import serializers
from django.http import JsonResponse


def home(request):
    recomended = Blog.objects.order_by('-timestamp')[0:6]
    blogs = Blog.objects.all()

    card = cardimage.objects.all().first()
    socials = social.objects.all().first()

    return render(request, 'index.html', {'recom': recomended, 'image': card, 'blog': blogs, 'social': socials})


def aboutC(request):
    infornation = about.objects.all().first()
    return render(request, 'about.html', {'information': infornation})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        messege = request.POST['messege']
        contact = Contact(name=name, email=email,
                          subject=subject, messege=messege)
        contact.save()
    contactss = contacts.objects.all().first()
    return render(request, 'contact.html', {'contact': contactss})


def search(request, cat):

    try:
        query = request.GET['keyword']
        Blogs = Blog.objects.filter(overview__icontains=query)
        messege = ""

    except:
        Blogs = Blog.objects.filter(categories=cat)
        messege = ""
        dict = {'1': 'Lifestyle', '2': 'Foods',
                '3': 'Guide', '4': 'Facts', '5': 'Fitness'}
        query = dict[cat]

    if len(Blogs) == 0:
        messege = f"oops! sorry there is no posts about {query}"

    return render(request, 'search.html', {'blog': Blogs, 'keyword': query, 'messege': messege})
