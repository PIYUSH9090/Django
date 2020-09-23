from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from chicago import models

# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display = ['subject','msg']
    search_fields = ['subject','msg']

admin.site.register(models.Notice, NoticeAdmin)

