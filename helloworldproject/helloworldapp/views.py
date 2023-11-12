from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworldview(request):
    return HttpResponse("Hello world from app.")