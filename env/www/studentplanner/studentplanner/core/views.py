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
        return HttpResponseRedirect(reverse('home'))
def logout1(request):
    if request.user.is_authenticated()==True:
        try:
            logout(request)
            del request.session['user_id']
        except KeyError:
            pass
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('login'))
def profile(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        useraccount = OrgAccount.objects.get(User = tempUser)
        if useraccount == None:
            useraccount = UserAccount.objects.get(User = tempUser) 
        return render_to_response('profile.html',{'tempUser':tempUser, 'useraccount':useraccount},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))    
def show_tasks(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        task_list = Task.objects.filter(owner = tempUser)
        clear_done_tasks(request)
        return render_to_response('tasks.html',{'task_list':task_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))
def show_events(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        event_list = Event.objects.filter(owner = tempUser)
        return render_to_response('events.html',{'event_list':event_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))
def show_notes(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        task_list = Task.objects.filter(owner = tempUser)
        event_list = Event.objects.filter(owner = tempUser)
        reminder_list = Reminder.objects.filter(owner = tempUser)
        return render_to_response('home.html',{'task_list':task_list, 'event_list':event_list, 'reminder_list': reminder_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))
def show_reminders(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        reminder_list = Reminder.objects.filter(owner = tempUser)
        return render_to_response('reminders.html',{'reminder_list':reminder_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))
def clear_done_tasks(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username__exact = request.session['username'])
        task_list1= Task.ojbects.filter(owner = tempUser)
        task_list2= []
        for a in task_list:
            if a.isDone == False:
                task_list2.append(a)
        return render_to_response('tasks.html',{'task_list2':task_list2},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('login'))    
def show_calendar(request):
	#if request.user.is_authenticated() = True:
		#tempUser = User.objects.get(username__exact = request.session['username'])
    return None
