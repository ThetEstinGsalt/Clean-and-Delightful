from django.shortcuts import render, HttpResponse
from .models import Contact


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        messege = request.POST['messege']
        contact = Contact(name=name, email=email,
                          subject=subject, messege=messege)
        contact.save()

    return render(request, 'contact.html')


def search(request, cat):
    print(cat)
    return render(request, 'search.html')
