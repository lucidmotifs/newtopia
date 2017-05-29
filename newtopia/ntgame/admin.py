from django.contrib import admin

from .models import Kingdom, Province, Military, Race, Infrastructure

# Register your models here.

# Game Entities
admin.site.register(Kingdom)
admin.site.register(Military)
admin.site.register(Race)
admin.site.register(Infrastructure)

class InfrastructureInline(admin.StackedInline):
    model = Infrastructure


@admin.register(Province)
class Province(admin.ModelAdmin):
    list_display = (
        'name',
        'ruler',
        'kingdom',
    )

    readonly_fields = ['owner_link']

    def owner_link(self, obj):
        change_url = urlresolvers.reverse('admin:auth_user_change',
            args=(obj.user.id,))

        return mark_safe('<a href="%s">%s</a>' % (change_url, obj.user.email))


    owner_link.short_description = 'Account'

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
            'fields': ('race', 'military', 'kingdom', owner_link, )
        }),
    )

    inlines = [
        InfrastructureInline,
    ]
