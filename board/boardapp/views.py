from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signupfunc(request):
    object = User.objects.all()
    print(object.email)

    if request.method == "POST":
        print("This is post method.")
    else:
        print("This is get method.")
    return render(request, "signup.html", {
        "some": 100
    })