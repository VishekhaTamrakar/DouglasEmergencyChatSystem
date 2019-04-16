from django.contrib import admin
from chat.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


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


@admin.register(PrivateChat)
class PrivateChatAdmin(ImportExportModelAdmin):
    pass

@admin.register(PrivateChatMessages)
class PrivateChatMessages(ImportExportModelAdmin):
    pass
