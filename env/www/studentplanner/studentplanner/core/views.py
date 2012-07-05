from django.http import HttpResponse, HttpResponseRedirect

def start_up(request):
	response = '<html><title>Student Planner</title> <center><strong><h1>SITE UNDER CONSTRUCTION!</h1><br><br></strong></center><body>This site will be constructed as a completion to the CS172 class of UP Diliman in cooperation with Google and AITI-MIT. The project is called S-Plan, short for student planner, which is an application that will help students organize their priorities for the whole term. The said app can also suggest activities for the student during his/her free time.</body></html>'
	return HttpResponse(response)
