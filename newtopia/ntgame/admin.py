from django.contrib import admin

from .models import Kingdom, Province, Army

# Register your models here.
admin.site.register(Kingdom)
admin.site.register(Province)
admin.site.register(Army)
