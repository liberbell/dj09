from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import TodoModel

# Create your views here.
class Todolist(ListView):
    template_name = "list.html"
    model = TodoModel

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = TodoModel

class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel
    success_url = reverse_lazy("list")

    fields = ["title", "memo", "priority", "due_date"]