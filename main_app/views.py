from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from forms import RegisterForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Volume, Chapter, Exercise, Solution
from django import forms


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
                error_message = "Oops, that's not a match."
                return render(request,"login.html",{'login_form': login_form, 'error_message': error_message})
        else:
            return render(request,"login.html",{'login_form': login_form})
    else:
        login_form = LoginForm()
    return render(request,"login.html",{'login_form': login_form})


def logoutme(request):
    logout(request)
    return HttpResponseRedirect('/main_app')


def profile(request):
    if request.POST:
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            user = User.objects.get(username=request.user.username)
            user.first_name = profile_form.cleaned_data['first_name']
            user.last_name = profile_form.cleaned_data['last_name']
            user.save()
        else:
            return render(request,"profile.html",{'profile_form': profile_form})
    else:
        profile_form = ProfileForm()
    return render(request,"profile.html",{'profile_form': profile_form})


@login_required
def volumes(request):
    volumes = Volume.objects.all()
    chapters = {}
    for volume in volumes:
        chapters[volume.id] = Chapter.objects.filter(volume = volume.id)
    return render(request,"volumes.html",{'volumes': volumes,'chapters': chapters})

@login_required
def chapters(request, chapter_id):
    chapter = get_object_or_404(Chapter, pk = chapter_id)
    exercises = Exercise.objects.filter(chapter = chapter_id)
    return render(request, "chapters.html",{'chapter': chapter, 'exercises': exercises})

@login_required
def exercises(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk = exercise_id)
    solution = Solution.objects.get(exercise = exercise_id)
    return render(request, "exercises.html",{'exercise': exercise, 'solution': solution})


