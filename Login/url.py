from django.urls import path,include
from django.conf.urls import url
from Login import views

urlpatterns = [
    url(r"sign-up.html",views.logup),
    url(r"forgot.html",views.forgetPassword),
    url(r"signOut.html",views.signOut),
    url(r"",views.index),
]