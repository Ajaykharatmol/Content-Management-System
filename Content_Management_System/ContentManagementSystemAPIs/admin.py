from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import RegisterUser,Task
    


admin.site.register(RegisterUser)
admin.site.register(Task)

