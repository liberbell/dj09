from django.shortcuts import render

# Create your views here.
def signupfunc(request):

    if request.method == "POST":
        print("This is post method.")
    else:
        print("This is get method.")
    return render(request, "signup.html", {
        "some": 100
    })