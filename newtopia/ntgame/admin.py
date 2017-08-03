from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Kingdom, Province, Military, Race
from .models import Infrastructure, InfrastructureItem, Building
from .models import Effect

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Military)
admin.site.register(Race)
admin.site.register(Infrastructure)
admin.site.register(Building)
#admin.site.register(EffectInstance)

class InfrastructureInline(admin.StackedInline):
    model = Infrastructure

    show_change_link = True
    can_delete = False

    readonly_fields = ('explored','built',)
    verbose_name_plural = "Infrastructure"

    fieldsets = (
    (None, {
        'fields': (
            'land',
        )
    }),
        ('Details', {
            'fields': (
                'built',
                'explored',
            )
        }),
    )


class MilitaryInline(admin.StackedInline):
    model = Military

    show_change_link = True
    can_delete = False

    verbose_name_plural = "Military"

@admin.register(Effect)
class Effect(admin.ModelAdmin):
    list_display = (
        'tag',
        'name',
    )

@admin.register(Province)
class Province(admin.ModelAdmin):
    list_display = (
        'name',
        'ruler',
        'kingdom',
    )

    readonly_fields = ('owner','trade_balance',)

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'ruler',
                'peasants',
                'money',
                'land',
                'food',
                'trade_balance',
            )
        }),
        ('Resources', {
            'fields': ('mages', 'runes', 'warhorses', 'prisoners',)
        }),
        ('Meta', {
            'fields': ('race', 'kingdom', 'owner', )
        }),
    )

    inlines = [
        InfrastructureInline, MilitaryInline
    ]
