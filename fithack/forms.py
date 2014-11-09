from django import forms
from models import Group
from django.forms import ModelForm

class GroupForm(ModelForm):
     class Meta:
         model = Group