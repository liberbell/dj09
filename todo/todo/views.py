from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TodoModel

# Create your views here.
class Todolist(ListView):
    template_name = "list.html"
    model = TodoModel

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel