from django.shortcuts import render, redirect
from fithack.forms import GroupForm


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/epochs")
    else:
        form = GroupForm()
    data = {'form': form}
    return render(request, "Epoch/new_epoch.html", data)