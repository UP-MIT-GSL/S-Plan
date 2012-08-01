from django.contrib.auth.models import User
from studentplanner.core.models import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

@csrf_exempt
def sigup_user(request):
	firstname = lastname = birthday = school = organization = gmail = webmail = ''
    
	if 'fname' in request.POST:
		firstname = request.POST['fname']
	if 'lname' in request.POST:
		lastname = request.POST['lname']
	if 'bday' in request.POST:
		birthday = request.POST['bday']
	if 'school' in request.POST:
		school = request.POST['school']
	if 'organization' in request.POST:
		organization = request.POST['organization']
	if 'gmailAddr' in request.POST:
		gmail = request.POST['gmailAddr']
	if 'univMailAddr' in request.POST:
		webmail = request.POST['univMailAddr']
	#add to the database.
@csrf_exempt
def sigup_org(request):
	orgname = orgtype = orghead = orgadd = orgGmailAddr = ''
    
	if 'orgname' in request.POST:
		orgname = request.POST['orgname']
	if 'orgtype' in request.POST:
		orgtype = request.POST['orgtype']
	if 'orghead' in request.POST:
		orghead = request.POST['orghead']
	if 'orgadd' in request.POST:
		orgadd = request.POST['orgadd']
	if 'orgGmailAddr' in request.POST:
		orgGmailAddr = request.POST['orgGmailAddr']
	#add to the database.
	
def login1(request):
    if request.user.is_authenticated()==False:
        context_instance={}
        context_instance.update(csrf(request))
        username = password = ''
        if request.method== "POST":
            if 'username' in request.POST:
                username = request.POST['username']
                password = request.POST['password']
                user= authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        request.session['username']=username          
                        return HttpResponseRedirect('/home')
                else:
                    return HttpResponseRedirect('/login')
            else:
                    return HttpResponseRedirect('/login')
        else:
            return render_to_response('login.html',{'username':username},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/home')
def logout1(request):
    if request.user.is_authenticated()==True:
        try:
            logout(request)
            del request.session['user_id']
        except KeyError:
            pass
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')
def profile(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username= request.session['username'])
        useraccount = OrgAccount.objects.get(orgname = tempUser)
        if useraccount == None:
            useraccount = UserAccount.objects.get(username = tempUser) 
        return render_to_response('profile.html',{'tempUser':tempUser, 'useraccount':useraccount},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')    
def show_tasks(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username = request.session['username'])
        task_list = Task.objects.filter(owner = tempUser)
        clear_done_tasks(request)
        return render_to_response('tasks.html',{'task_list':task_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')
def show_events(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username = request.session['username'])
        event_list = Event.objects.filter(owner = tempUser)
        return render_to_response('events.html',{'event_list':event_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')
def show_notes(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username = request.session['username'])
        task_list = Task.objects.filter(owner = tempUser)
        event_list = Event.objects.filter(owner = tempUser)
        reminder_list = Reminder.objects.filter(owner = tempUser)
        return render_to_response('user_home.html',{'task_list':task_list, 'event_list':event_list, 'reminder_list': reminder_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')
def show_reminders(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username = request.session['username'])
        reminder_list = Reminder.objects.filter(owner = tempUser)
        return render_to_response('reminders.html',{'reminder_list':reminder_list},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')
def clear_done_tasks(request):
    if request.user.is_authenticated() == True:
        tempUser = User.objects.get(username = request.session['username'])
        task_list1= Task.ojbects.filter(owner = tempUser)
        task_list2= []
        for a in task_list:
            if a.isDone == False:
                task_list2.append(a)
        return render_to_response('tasks.html',{'task_list2':task_list2},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')    
def show_calendar(request):
    return None
