from django.shortcuts import render, redirect
from fithack.forms import GroupForm
from fithack.models import Group, Data
import operator

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


