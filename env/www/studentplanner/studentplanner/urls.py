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
    #url(r'^$', TemplateView.as_view(template_name="login.html"), name="login"),
    url(r'^profile/$', TemplateView.as_view(template_name="profile.html"), name="profile"),
    #url(r'^logout/$', TemplateView.as_view(template_name="logout.html"), name="logout"),
    url(r'^calendar/$', TemplateView.as_view(template_name="calendar.html"), name="calendar"),
    url(r'^tasks/$', TemplateView.as_view(template_name="task.html"), name="task"),
    url(r'^reminders/$', TemplateView.as_view(template_name="reminders.html"), name="reminder"),
    url(r'^events/$', TemplateView.as_view(template_name="events.html"), name="event"),
    url(r'^home/$', TemplateView.as_view(template_name="user_home.html"), name="home"),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name="contact"),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
