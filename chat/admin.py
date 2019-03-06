from django.contrib import admin
from chat.models import *
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    '''Chat room'''
    list_display = ("creater", "invited_user", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])

class ChatAdmin(admin.ModelAdmin):
    '''Dialogs'''
    list_display = ("room", "user", "text", "date")

admin.site.register(Event, EventAdmin)
admin.site.register(Chat, ChatAdmin)