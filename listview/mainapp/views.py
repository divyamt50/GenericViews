from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic import ListView, DetailView
from django.apps import apps
from django.urls import reverse
# Create your views here.

class MainView(View):
    def get(self, request):
        model_urls = []
        models = [Cat]
        
        for model in models:
            model_name = model.__name__
            model_url = reverse(f'mainapp:{model_name.lower()}_list')
            model_urls.append((model_name, model_url))
            
        context = {'model_urls': model_urls}
        return render(request, 'mainapp/main.html', context)


class CatsView(ListView):
    model = Cat
    template_name = 'mainapp/catlist.html'
    context_object_name = 'cats'

class CatDescription(DetailView):
    model = Cat
    template_name = 'mainapp/catdesc.html'
    context_object_name = 'cat'