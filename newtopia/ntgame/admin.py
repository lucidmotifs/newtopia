from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Kingdom, Province, Military, Race, Infrastructure

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Military)
admin.site.register(Race)
admin.site.register(Infrastructure)

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
            'fields': ('race', 'military', 'kingdom', 'owner', )
        }),
    )

    inlines = [
        InfrastructureInline,
    ]
