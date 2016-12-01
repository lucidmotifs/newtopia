from django.contrib import admin

from .models import Rule, NetworthValue

# Register your models here.

# Meta Objects
@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass


@admin.register(NetworthValue)
class NetworthValue(admin.ModelAdmin):
    list_display = ('prop', 'value')
