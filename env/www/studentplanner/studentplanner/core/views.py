# Create your views here.
from django.contrib.auth.models import User
from studentplanner.core.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def start_up(request):
    html='<html><h1><strong><center>SITE UNDER CONSTRUCTION</center></strong></h1><br><p></p></html>'
    return HttpResponse(html)
def login1(request):
    if request.user.is_authenticated()==False:
        context_instance={}
        context_instance.update(csrf(request))
        username = password = ''
        if request.method== "POST":
            username = request.POST['username']
            password = request.POST['password']
            user= authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    request.session['username']=username            
                    return HttpResponseRedirect('/%s'%username)
            else:
                return HttpResponseRedirect('')
        else:
            return render_to_response('login.html',{'username':username},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('')
def logout1(request):
    if request.user.is_authenticated()==True:
        try:
        logout(request)
        del request.session['user_id']
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect()
def profile(request):
    tempUser = User.objects.get(username__exact = request.session['username'])
    return None
def show_task(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        task_list = Task.objects.filter(owner = tempUser)
    else:
        return HttpResponseRedirect()
def show_events(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        event_list = Event.objects.filter(owner = tempUser)
    else:
        return HttpResponseRedirect()
def show_notes(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        note_list = Note.objects.filter(owner = tempUser)
    else:
        return HttpResponseRedirect()
def show_reminders(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        reminder_list = Reminder.objects.filter(owner = tempUser)
    else:
        return HttpResponseRedirect()
def clear_done_tasks(request):
    return None
def show_calendar(request):
    return None
