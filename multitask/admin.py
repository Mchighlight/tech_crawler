from django.contrib import admin

from .models import Cronjob

class CronjobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'trigger_time')
    list_filter = ('name',)
    search_field = ('name')

admin.site.register(Cronjob, CronjobAdmin)

