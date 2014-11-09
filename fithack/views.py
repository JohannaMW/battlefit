from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, render_to_response
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from fit import settings
from fithack.forms import EmailUserCreationForm
from fithack.models import *
# from fithack.forms import *


def home(request):
    return render_to_response("home.html")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("profile")
    else:
        form = EmailUserCreationForm()
    return render(request, "registration/register.html", {'form': form})

@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("registration/login")
    return render(request, "registration/profile.html")


def user_dashboard(request):
    return render(request, 'user_dashboard.html')
