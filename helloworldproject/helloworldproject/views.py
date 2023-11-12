from pathlib import Path
from django.http import HttpResponse
from django.views.generic import TemplateView

def someview(request):
    print(Path(__file__).resolve().parent.parent)
    return HttpResponse("")

def helloworldfunction(request):
    returned_object = HttpResponse("<h1>Hello World</h1>")

    return returned_object

class HelloWorldClass(TemplateView):
    template_name = "hello.html"