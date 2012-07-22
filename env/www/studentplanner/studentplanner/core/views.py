# Create your views here.
from django.http import HttpResponse

def start_up(request):
    html='<html><h1><strong><center>SITE UNDER CONSTRUCTION</center></strong></h1><br><p></p></html>'
    return HttpResponse(html)
def login(request):
    return None
def profile(request, username):
    return None
def show_task(request):
    return None
def show_events(request):
    return None
def show_notes(request):
    return None
def show_reminders(request):
    return None
def clear_done_tasks(request):
    return None
def logout(request):
    return None
def show_calendar(request):
    return None
