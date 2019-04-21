from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'website', 'address', 'upload_time', 'photo_url', 'topic')
    list_filter = ('website', 'topic')
    search_field = ('subject', 'website')
    list_per_page = 20

admin.site.register(Article, ArticleAdmin)
