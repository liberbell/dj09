from django.urls import path
from .views import Todolist, TodoDetail

urlpatterns = [
    path("list/", Todolist.as_view(), name="list"),
    path("detail/<int:pk>", TodoDetail.as_view(), name="detail"),
]