from django.urls import path
from .views import Todolist

urlpatterns = [
    path("list/", Todolist.as_view(), name="list"),
]