from django.contrib import admin

from .models import *


#Property
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'addressShort', 'addressFull', 'slug')
admin.site.register(Property, PropertyAdmin)

class PropertyActivityAdmin(admin.ModelAdmin):
    list_display    = ('prop', 'type', 'priority', 'activity_on')
    ordering        = ["-activity_on"]

admin.site.register(PropertyActivity, PropertyActivityAdmin)


class AccessDeviceAdmin(admin.ModelAdmin):
    list_display = ('label', 'label')
admin.site.register(AccessDevice, AccessDeviceAdmin)

class AssetAdmin(admin.ModelAdmin):
    list_display = ('label', 'label')
admin.site.register(Asset, AssetAdmin)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ()
admin.site.register(Feature, FeatureAdmin)

class FeatureOptionAdmin(admin.ModelAdmin):
    list_display = ('label', 'groupMain', 'groupSub')
admin.site.register(FeatureOption, FeatureOptionAdmin)

class VendorServiceAdmin(admin.ModelAdmin):
    list_display = ('label', 'label')
admin.site.register(VendorService, VendorServiceAdmin)


class LeaseAdmin(admin.ModelAdmin):
    list_display = ('prop', 'dateLeaseStart', 'dateLeaseEnd', 'daysInLease', 'daysRemaining')
admin.site.register(Lease, LeaseAdmin)

class FeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'defaultAmount')
admin.site.register(Fee, FeeAdmin)

class LeaseFeeAdmin(admin.ModelAdmin):
    list_display = ('lease', 'fee', 'amount')
admin.site.register(LeaseFee, LeaseFeeAdmin)

class LeaseContactAdmin(admin.ModelAdmin):
    list_display = ('lease', 'contact', 'type')
admin.site.register(LeaseContact, LeaseContactAdmin)

class PropertyOwnerAdmin(admin.ModelAdmin):
    list_display = ('prop', 'contact', 'type')
    ordering        = ["contact", "prop"]
admin.site.register(PropertyOwner, PropertyOwnerAdmin)


