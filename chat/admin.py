from django.contrib import admin
from chat.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# class EventAdmin(admin.ModelAdmin):
#     '''Chat room'''
#     list_display = ("creater", "invited_user", "date")
#
#     def invited_user(self, obj):
#         return "\n".join([user.username for user in obj.invited.all()])
#
# class ChatAdmin(admin.ModelAdmin):
#     '''Dialogs'''
#     list_display = ("room", "user", "text", "date")

class EventResources(resources.ModelResource):

    class Meta:
        model = Event
        list_display = ("creater", "invited_user", "date")

        def invited_user(self, obj):
            return "\n".join([user.username for user in obj.invited.all()])


class ChatResources(resources.ModelResource):
    '''Dialogs'''
    class Meta:
        model = Chat
        list_display = ("room", "user", "text", "date")


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    pass

@admin.register(Chat)
class ChatAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(Event, EventAdmin)
#admin.site.register(Chat, ChatAdmin)