from django.contrib import admin

from uploadfile.models import Profile
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Profile,ProfileAdmin)
