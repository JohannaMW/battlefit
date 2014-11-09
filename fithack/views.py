from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render, render_to_response
from django.core.mail import EmailMultiAlternatives
from fit import settings
from fithack.models import *
# from fithack.forms import *


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