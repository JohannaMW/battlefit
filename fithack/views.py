from fithack.forms import GroupForm
import operator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, render_to_response
from django.core.mail import EmailMultiAlternatives
from fit import settings
from fithack.models import *

def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/epochs")
    else:
        form = GroupForm()
    data = {'form': form}
    return render(request, "create_group.html", data)

def group(request, group_id):
    group = Group.objects.get(id=group_id)
    data = Data.objects.filter(member = request.user, date__range=[group.start_date, group.end_date])
    member_data = []
    data_group = []
    score = 0
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
            mem_score = (group.goal - member_avg) / group.goal
            member_score[member.username] = mem_score
            print member_score

    elif group.category == 'H':
        for datum in data:
            data_group.append(datum.calories_consumed)
        data_h = sum(data_group)/len(data_group)
        score = (data_h - group.goal) / data_h
        members = group.member
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
    winner_score = sorted_scores[1]
    print winner_score
    winner_name = sorted_scores[0]
    print winner_name

    data = {
        "group_avg":group_avg,
        "score":score,
        "group":group,
        "winner_score" : winner_score,
        "winner_name" : winner_name
    }

    return render(request, "group.html", data)


def home(request):
    return render_to_response("home.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            # <h2>Thanks {} for signing up!</h2> <div>I hope you enjoy using our site</div>
            html_content = '<div style="width:500px;"><table width="100%" border="0" align="center" cellpadding="5" style="background: #ffffff; border-right: 1px solid #cccccc; border-left: 1px solid #cccccc; border-top: 1px solid #cccccc; border-bottom: 1px solid #cccccc;"><tr><td valign="bottom"><table width="100%" height="75px;" border="0" style=" background-color:#285e8e; padding-left:10px;"><tr><td align="left" valign="bottom"><span style="color:#fff; padding-bottom:5px; font-size:22px; font-family:Arial, Helvetica, sans-serif; letter-spacing:2px;"><strong>PROPERTY MANAGER</strong></span></td></tr></table></td></tr><tr><td><div style="padding:5px; color:#555555; font-family: Arial, Helvetica, sans-serif;"><h2>Hi {}, thank you for signing up!</h2> I hope you enjoy using our site!</div></td></tr><tr><td><table width="100%" height="20px;" border="0" style=" background-color:#285e8e;"><tr><td align="left" valign="bottom">&nbsp;</td></tr></table></td></tr></table></div>'.format(user.username)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("/profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def profile(request):
    if not request.user.is_authenticated():
        return redirect("registration/login")
    return render(request, "registration/profile.html")


def user_dashboard(request):
    return render(request, 'user_dashboard.html')

