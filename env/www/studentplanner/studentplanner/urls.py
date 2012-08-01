from django.conf.urls import patterns, include, url
from studentplanner.core import views
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentplanner.views.home', name='home'),
    # url(r'^studentplanner/', include('studentplanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login1, name=""),
    url(r'^login/$', views.login1, name="login"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^logout/$', views.logout1, name="logout"),
    url(r'^calendar/$', TemplateView.as_view(template_name="calendar.html"), name="calendar"),
    url(r'^tasks/$', views.show_tasks, name="task"),
    url(r'^reminders/$',views.show_reminders, name="reminder"),
    url(r'^events/$', views.show_events, name="event"),
    url(r'^home/$', views.show_notes, name="home"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
	url(r'^signup/$', TemplateView.as_view(template_name="signup.html"), name="signup"),
	url(r'^signup_user/$', '''views.signup_user'''TemplateView.as_view(template_name="signup_user.html"), name="usersignup"),
	url(r'^signup_org/$', '''views.signup_org'''TemplateView.as_view(template_name="signup_org.html"), name="orgsignup"),
	url(r'^addNote/$', TemplateView.as_view(template_name="addNote.html"), name="addnote"),
	url(r'^addEvent/$', TemplateView.as_view(template_name="addEvent.html"), name="addevent"),
	url(r'^addTask/$', TemplateView.as_view(template_name="addTask.html"), name="addtask"),
	url(r'^addReminder/$', TemplateView.as_view(template_name="addReminder.html"), name="addreminder"),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
