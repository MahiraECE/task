from django.shortcuts import render
from django.views.generic import ListView, CreateView # new
from .models import Brand,Category
# Create your views here.

#Views to render Category details
class categoryPageView(ListView):
    model = Category
    template_name = 'category.html'
#Views to render Brand details

class brandsPageView(ListView):
    model = Brand
    template_name = 'brand.html'
