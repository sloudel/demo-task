from django.contrib import admin
from .models import *
# Register your models here.

class ContentInline(admin.TabularInline):
    model = Content

class PageAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        ContentInline,
    ]

class ContentAdmin(admin.ModelAdmin):
    search_fields = ['title']
    

admin.site.register(Page, PageAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Text)



