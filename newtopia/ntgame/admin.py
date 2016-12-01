from django.contrib import admin

from .models import Kingdom, Province, Army, Race

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Province)
admin.site.register(Army)
admin.site.register(Race)
