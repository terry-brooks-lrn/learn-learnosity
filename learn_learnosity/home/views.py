from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from assessment.learnosity import generated_request_Items


def home(request):
    return render(request, 'home.html', {"title": "Home"})


def about(request):
    context = dict()
    context['title'] = "About Learnosity & Assessment Project"
    context['generated_request'] = generated_request_Items
    return render(request, 'about.html', context)

def root(request):
    return redirect(home)