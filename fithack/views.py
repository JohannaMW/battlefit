import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, render_to_response
from django.core.mail import EmailMultiAlternatives
from django.views.decorators.csrf import csrf_exempt
from fithack.forms import EmailUserCreationForm


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

@csrf_exempt
def new_calories_consume(request):
    print "new_calories_consume works"
    if request.method == 'POST':
        data = json.loads(request.body)
        print data

    return HttpResponse(content_type='application.json')

@csrf_exempt
def new_calories_burned(request):
    print "new_calories_burned works"
    if request.method == 'POST':
        data = json.loads(request.body)
        print data

    return HttpResponse(content_type='application.json')

@csrf_exempt
def new_body_fat(request):
    print "new_body_fat works"
    if request.method == 'POST':
        data = json.loads(request.body)
        print data

    return HttpResponse(content_type='application.json')
