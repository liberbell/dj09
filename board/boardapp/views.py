from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username, "", password)
            return render(request, "signup.html", {
                "some": 100
            })
        except IntegrityError:
            return render(request, "signup.html", {"error": "User already exists"})
    return render(request, "signup.html")

def loginfunc(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            return render(request, "login.html",
                          {})
    return render(request, "login.html", {})

@login_required
def listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, "list.html", {
        "object_list": object_list
    })

def logoutfunc(request):
    logout(request)
    return redirect("login")

def detailfunc(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    print(object)
    return render(request, "detail.html", {'object': object})

def goodfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += object.good
    object.save()
    return redirect("list")

def readfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if username in object.read_text:
        return redirect("list")
    else:
        object.read += object.read
        object.read_text = object.read_text + " " + username