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
    if group.category == 'W':
        data_group = data.calories_burned
        data_w = sum(data_group)/len(data_group)
        score = (group.goal - data_w) / group.goal
    elif group.category == 'H':
        data_group = data.calories_consumed
        data_h = sum(data_group)/len(data_group)
        score = (data_h - group.goal) / data_h
    else:
        data_group = data.
        data_f = sum(data_group)/len(data_group)

