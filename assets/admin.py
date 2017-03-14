from django.contrib import admin

from .models import *


class KeyCabinetAdmin(admin.ModelAdmin):
    list_display    = ('label', 'notes')
    ordering        = ["label"]
admin.site.register(KeyCabinet, KeyCabinetAdmin)


class KeyCabinetSpotAdmin(admin.ModelAdmin):
    list_display    = ('cabinet', 'number')
    ordering        = ['cabinet', 'number']
admin.site.register(KeyCabinetSpot, KeyCabinetSpotAdmin)


class ReservedKeyAdmin(admin.ModelAdmin):
    list_display    = ('prop', 'spot', 'location', 'last_update_date', 'last_update_contact')
    ordering        = ['prop']
admin.site.register(ReservedKey, ReservedKeyAdmin)

class LockBoxAdmin(admin.ModelAdmin):
    list_display    = ('serial', 'prop', 'last_update_date', 'last_update_contact')
    ordering        = ['serial']
admin.site.register(LockBox, LockBoxAdmin)
