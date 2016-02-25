from django.shortcuts import render, redirect
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def main(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():   
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,"main.html")
                else:
                    return HttpResponse("You account has been blocked")
            else:
                return render(request,"main.html",{'login_form': login_form})
        else:
            return render(request,"login.html",{'login_form': login_form})
    else:
        login_form = LoginForm()
    return render(request,"main.html",{'login_form': login_form})


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            login_form = LoginForm(initial={"username": username})
            return render(request,"login.html",{'login_form': login_form})
    else:
        register_form = RegisterForm()
    return render(request,"register.html",{'register_form': register_form})


def logme(request):
    if request.GET:
        next = request.GET['next']
        print(next)
    if request.POST:
        next = ""
        split_referer = request.META['HTTP_REFERER'].split("next=")
        if len(split_referer) == 2:
            next = split_referer[1]  
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if next == "":
                        return HttpResponseRedirect('/main_app')
                    else:
                        return HttpResponseRedirect(next)
                else:
                    return HttpResponse("You account has been blocked")
            else:
                return render(request,"login.html",{'login_form': login_form})
        else:
            return render(request,"login.html",{'login_form': login_form})
    else:
        login_form = LoginForm()
    return render(request,"login.html",{'login_form': login_form})

    
def logoutme(request):
    logout(request)
    return HttpResponseRedirect('/main_app')
    
@login_required
def chapter_list(request):
    return render(request,"chapter_list.html")