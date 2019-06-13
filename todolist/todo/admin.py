from django.contrib import admin
from .models import List
from django.db import models


class ListAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Content", {'fields': ["item", "completed"]}),
    ]

admin.site.register(List)
