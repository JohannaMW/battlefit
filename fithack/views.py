from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def user_dashboard(request):
    return render(request, 'user_dashboard.html')