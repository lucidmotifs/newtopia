from django.contrib import admin

from .models import EntityGroup, Entity, Aspect

# Register your models here.

# Meta Objects
@admin.register(EntityGroup)
class RuleAdmin(admin.ModelAdmin):
    pass


@admin.register(Entity)
class NetworthValue(admin.ModelAdmin):
    pass


@admin.register(Aspect)
class NetworthValue(admin.ModelAdmin):
    pass
