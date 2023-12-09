from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'
