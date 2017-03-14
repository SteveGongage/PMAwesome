from django.contrib import admin

from .models import Contact
from .models import Message

#Message
class MessageAdmin(admin.ModelAdmin):
	list_display = ('fromName', 'subject', 'id')

admin.site.register(Message, MessageAdmin)


#Contact
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nameFull', 'nameFirst', 'isOwner', 'isTenant', 'isStaff', 'isAdmin', 'id')

admin.site.register(Contact, ContactAdmin)