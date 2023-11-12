from django.urls import path
from .views import helloworlappdview

urlpatterns = [
    path("helloworldapp/", helloworlappdview),
]
