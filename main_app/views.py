from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class MainView(TemplateView):
    template_name = "main.html"


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            return render(request,"login.html")
    else:
        form = RegisterForm()
    return render(request,"register.html",{'register_form': form})


def log_me_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        form = LoginForm(request.POST)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,"main.html")
            else:
                return HttpResponse("You account has been blocked")
        else:
            return render(request,"login",{'login_form': form})
    else:
        form = LoginForm()
    return render(request,"login",{'login_form': form})

@login_required
def logout(request):
    logout(request)