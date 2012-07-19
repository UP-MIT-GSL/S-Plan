from django.db import models
from django.contrib.auth.models import User
class OrgAccount(models.Model):
    orgname = models.ForeignKey(User, related_name= 'Orgname')
    orgHead = models.CharField(max_length=50)
    orgAdviser = models.CharField(max_length=50)
    orgAdd = models.CharField(max_length=150)
    def __unicode__(self):
        return "%s"%orgname
class UserAccount(models.Model):
    username = models.ForeignKey(User, related_name= 'Username')
    birthday = models.DateField()
    university = models.CharField(max_length=100)
    organization = models.ForeignKey(OrgAccount, related_name="Orgname")
    webmail = models.CharField(max_length=100)
    def __unicode__(self):
        return "%s"%username
class Tasks(models.Model):
    task = models.CharField(max_length=50)
    start= models.DateField(auto_now_add = True)
    end= models.DateField()
    subject = models.CharField(max_length=50)
    def __unicode__(self):
        return "%s"%task
class Event(models.Model):
    event = models.CharField(max_length=50)
    start= models.DateField(auto_now_add = True)
    end= models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=150)
    def __unicode__(self):
        return "%s"%event
class Reminder(models.Model):
    reminder = models.CharField(max_length=50)
    start= models.DateField(auto_now_add = True)
    end= models.DateField()
    def __unicode__(self):
        return "%s"%reminder
class Notes(models.Model):
    note = models.CharField(max_length=50)
    body = models.CharField(max_length=5000)
    start= models.DateField(auto_now_add = True)
    end= models.DateField()
    def __unicode__(self):
        return "%s"%note
