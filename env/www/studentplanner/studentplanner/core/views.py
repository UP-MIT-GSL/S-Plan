from django.http import HttpResponse, HttpResponseRedirect

def start_up(request):
	response = '<html><title>Student Planner</title> <strong><h1>SITE UNDER CONSTRUCTION</h1></strong></html>'
	return HttpResponse(response)
