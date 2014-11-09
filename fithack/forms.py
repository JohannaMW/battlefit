from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from fithack.models import *
from django.forms import ModelForm


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Member
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Member.objects.get(username=username)
        except Member.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class GroupForm(ModelForm):
    class Meta:
        model = Group


class GroupAdminForm(ModelForm):
    class Meta:
        model = GroupAdmin


class DataForm(ModelForm):
    class Meta:
        model = Data
