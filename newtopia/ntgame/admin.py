from django.contrib import admin

from .models import Kingdom, Province, Military, Race

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Province)
admin.site.register(Military)
admin.site.register(Race)
