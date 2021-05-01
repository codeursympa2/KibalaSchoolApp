from django.shortcuts import render,redirect

# Create your views here.
def login_blog(request):
    return render(request,"login.html")