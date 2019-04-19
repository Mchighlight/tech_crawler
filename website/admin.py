from django.contrib import admin

from .models import SearchItem, Website

class WebsiteAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name'  )
    list_filter = ( 'name', )
    search_field = ( 'name', 'descripttion' )

class SearchItemAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'name' )
    list_filter  = ('name',)

admin.site.register(Website, WebsiteAdmin)
admin.site.register(SearchItem, SearchItemAdmin)
