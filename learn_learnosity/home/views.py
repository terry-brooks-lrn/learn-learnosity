from django.shortcuts import render
from django.views.generic import TemplateView



def home(request):
    return render(request, 'home.html', {"title": "Home"})
