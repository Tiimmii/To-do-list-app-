from django.contrib import admin
from . models import Task, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Task)
admin.site.register(User, UserAdmin)
