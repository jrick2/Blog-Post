from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from users.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import User
from myblog import templates
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        
        else:
            return render(request, "login.html", {
                "message": "Username or Password Is Incorrect"
            })

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html")

def sign_up(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponseRedirect(reverse("home"))
	else:
	    form = NewUserForm()
	return render (request, "sign-up.html", context={"form":form})