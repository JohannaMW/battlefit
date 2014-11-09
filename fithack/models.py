from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    FEMALE = 'F'
    MALE = 'M'
    score = models.IntegerField()
    name = models.CharField(max_length=200)
    pic = models.ImageField()
    weight = models.FloatField()
    height = models.IntegerField()
    GENDER_CHOICES = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()

class Group(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    goal = models.FloatField()

class GroupAdmin(models.Model):
    admin = models.BooleanField(default=False)
    user = models.ForeignKey(Member, related_name='administrator')
    group = models.ForeignKey(Group, related_name='administrator')

class Data(models.Model):
    calories_consumed = models.FloatField()
    calories_burned = models.FloatField()
    date = models.DateField()
    activity = models.CharField(max_length=200)
    member = models.ForeignKey(Member, related_name='data')
