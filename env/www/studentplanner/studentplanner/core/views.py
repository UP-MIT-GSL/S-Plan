# Create your views here.
from django.http import HttpResponse

def start_up(request):
    html='<html><h1><strong><center>SITE UNDER CONSTRUCTION</center></strong></h1><br><p></p></html>'
    return HttpResponse(html)
def login(request):
def profile(request, username):
def show_task(request):
def show_events(request):
def show_notes(request):
def show_reminders(request):
def clear_done_tasks(request):
def logout(request):
def show_calendar(request):
