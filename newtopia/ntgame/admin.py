from django.contrib import admin

from .models import Kingdom, Province, Military, Race

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Military)
admin.site.register(Race)

@admin.register(Province)
class Province(admin.ModelAdmin):
    list_display = (
        'name',
        'ruler',
        'kingdom',
    )

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
            'fields': ('race', 'military', 'kingdom', 'owner',)
        }),
    )
