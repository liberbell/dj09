from pathlib import Path
from django.http import HttpResponse

def someview(request):
    print(Path(__file__).resolve().parent.parent)
    return HttpResponse("")