from django.contrib import admin
from models import *
admin.site.register(UserAccount)
admin.site.register(OrgAccount)
admin.site.register(Task)
admin.site.register(Event)
admin.site.register(Note)
admin.site.register(Reminder)

