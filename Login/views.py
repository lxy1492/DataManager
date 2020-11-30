from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"login/index.html")

def logup(request):
    return render(request,"login/sign-up.html")

def forgetPassword(request):
    return render(request,"login/forgot.html")

def signOut(request):
    return render(request,"login/signOut.html")