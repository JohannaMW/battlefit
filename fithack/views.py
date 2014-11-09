from django.shortcuts import render, redirect
from fithack.forms import GroupForm
from fithack.models import Group, Data

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
    data = Data.objects.get(member = request.user, date__range=[group.start_date, group.end_date])
    member_data = []
    score = 0
    if group.category == 'W':
        data_group = data.calories_burned
        data_w = sum(data_group)/len(data_group)
        score = (group.goal - data_w) / group.goal
        members = group.member
        for member in members:
            data_member = Data.objects.get(member=member, date__range=[group.start_date, group.end_date])\
                .calories_burned
            member_data.append(data_member)

    elif group.category == 'H':
        data_group = data.calories_consumed
        data_h = sum(data_group)/len(data_group)
        score = (data_h - group.goal) / data_h
        members = group.member
        for member in members:
            data_member = Data.objects.get(member=member, date__range=[group.start_date, group.end_date])\
                .calories_consumed
            member_data.append(data_member)
    else:
        data_group = data.body_fat
        score = sum(data_group)/len(data_group)
        members = group.member
        for member in members:
            data_member = Data.objects.get(member=member, date__range=[group.start_date, group.end_date])\
                .body_fat
            member_data.append(data_member)

    group_avg = sum(member_data)/len(member_data)
    data = {
        "group_avg":group_avg,
        "score":score,
        "group":group
    }
    return render(request, "group.html", data)


