# Create your views here.
from django.http import HttpResponse

def start_up(request):
    html='<html><h1><strong><center>SITE UNDER CONSTRUCTION</center></strong></h1><br><p></p></html>'
    return HttpResponse(html)
