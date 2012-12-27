from django.contrib import admin
from models import *


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'


admin.site.register(Poll, PollAdmin)