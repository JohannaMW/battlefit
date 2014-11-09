import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html')


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