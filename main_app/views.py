from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .forms import RegisterForm

class MainView(TemplateView):
    template_name = "main.html"


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # process cleaned_data
            return render(request,"main.html")
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form': form})


def login(request):
    return render(request, "login.html")

#try:
#    validate_password(password)
#except ValidationError as ve:
#    print(ve)
#    raise ve
#    return render(request, "register.html")
#repeat_password = request.POST['repeat-password']
#print(username)
#print(email)
#return render(request, "main.html")