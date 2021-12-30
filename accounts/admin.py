from django.contrib import admin
from .models import Profile,Log
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','gender','nc', 'is_author')
    list_filter = ('user','gender')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('created',)
    list_filter = ('created',)
