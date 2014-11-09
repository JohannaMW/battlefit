from fithack.forms import GroupForm
import operator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from fithack.forms import EmailUserCreationForm
from fithack.models import *


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/create")
    else:
        form = GroupForm()
    data = {'form': form}
    return render(request, "create_group.html", data)


def group(request, group_id):
    group = Group.objects.get(id=group_id)
    data = Data.objects.filter(member = request.user, date__range=[group.start_date, group.end_date])
    member_data = []
    data_group = []
    member_score = {}

    if group.category == 'W':
        for datum in data:
            data_group.append(datum.calories_burned)
        data_w = sum(data_group)/len(data_group)
        score = (group.goal - data_w) / group.goal
        members = group.member.all()
        print members
        for member in members:
            member_dataset = []
            data = Data.objects.filter(member=member, date__range=[group.start_date, group.end_date])
            for d in data:
                member_dataset.append(d.calories_burned)
                member_data.append(d.calories_burned)
            member_avg = sum(member_dataset)/len(member_dataset)
            mem_score = group.goal - member_avg / group.goal
            member_score[member.username] = mem_score

    elif group.category == 'H':
        for datum in data:
            data_group.append(datum.calories_consumed)
        data_h = sum(data_group)/len(data_group)
        score = group.goal - data_h / group.goal
        members = group.member.all()
        for member in members:
            data = Data.objects.filter(member=member, date__range=[group.start_date, group.end_date])
            for d in data:
                member_data.append(d.calories_consumed)
    else:
        for datum in data:
            data_group.append(datum.body_fat)
        score = sum(data_group)/len(data_group)
        members = group.member
        for member in members:
            data = Data.objects.filter(member=member, date__range=[group.start_date, group.end_date])
            for d in data:
                member_data.append(d.body_fat)

    group_avg = sum(member_data)/len(member_data)
    sorted_scores = sorted(member_score.items(), key=operator.itemgetter(1))
    sorted_scores.reverse()
    winner = sorted_scores[0]


    data = {
        "group_avg":group_avg,
        "score":score,
        "group":group,
        "winner_score" : winner[1],
        "winner_name" : winner[0]
    }

    return render(request, "group.html", data)


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

