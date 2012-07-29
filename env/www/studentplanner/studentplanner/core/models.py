from django.db import models
from django.contrib.auth.models import User
class Event(models.Model):
    owner = models.ForeignKey(User, related_name='OwnerE')
    events = models.CharField(max_length=100)
    time = models.TimeField()
    end= models.DateField()
    venue = models.CharField(max_length=150)
    def __unicode__(self):
        return "%s"%(self.events)
class OrgAccount(models.Model):
    ORG_TYPES = (
        ('Acad','Academic'), 
        ('All','Alliance'), 
        ('CO','Cause-Oriented'), 
        ('CS','Community Service'), 
        ('Frat','Fraternity'),
        ('RP','Regional/Provincial'),
        ('Rel','Religious'),
        ('Soro','Sorority'),
        ('SI','Special Interest'),
        ('SR','Sports and Recreation'),
    )
    orgname = models.ForeignKey(User, related_name= 'Orgname')
    orgHead = models.CharField(max_length=50)
    orgAdd = models.CharField(max_length=150)
    orgType= models.CharField(max_length=100, choices=ORG_TYPES)
    members= models.ManyToManyField(User, related_name = 'Member')
    def __unicode__(self):
        return "%s"%(self.orgname)
class UserAccount(models.Model):
    username = models.ForeignKey(User, related_name= 'Username')
    birthday = models.DateField()
    university = models.CharField(max_length=100)
    organization = models.ManyToManyField(OrgAccount, related_name="Orgname")
    webmail = models.CharField(max_length=100)
    participating = models.ManyToManyField(Event, related_name="Participating")
    def __unicode__(self):
        return "%s"%(self.username)
class Task(models.Model):
    owner = models.ForeignKey(User, related_name='OwnerT')
    task= models.CharField(max_length=100)
    isDone= models.BooleanField()
    end= models.DateField()
    subject = models.CharField(max_length=50)
    def __unicode__(self):
        return "%s"%(self.task)
class Reminder(models.Model):
    owner = models.ForeignKey(User, related_name='OwnerR')
    reminder= models.CharField(max_length=50)
    occurence = models.DateField()
    def __unicode__(self):
        return "%s"%(self.reminder)

