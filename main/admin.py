from django.contrib import admin

from .models import Teams, TeamMembers, Tasks

# Register your models here.

admin.site.register(Teams)
admin.site.register(TeamMembers)
admin.site.register(Tasks)

