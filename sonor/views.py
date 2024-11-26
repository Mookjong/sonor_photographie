from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def home(request: HttpRequest):

    return render(request, 'sonor/pages/home.html', {
        'current_page': 'home'
    })


def about(request: HttpRequest):

    return render(request, 'sonor/pages/about.html', {
        'current_page': 'about'
    })


def portfolio(request: HttpRequest):

    return render(request, 'sonor/pages/gallery.html', {
        'current_page': 'gallery'
    })


def contact(request: HttpRequest):

    return render(request, 'sonor/pages/contact.html', {
        'current_page': 'contact'
    })





