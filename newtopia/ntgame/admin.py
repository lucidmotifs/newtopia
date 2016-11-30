from django.contrib import admin

from .models import Kingdom, Province, Army, Race, Rule

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Province)
admin.site.register(Army)
admin.site.register(Race)

# Meta Objects
#@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    class Meta:
        app_label = "ntmeta"

admin.site.register(Rule)
