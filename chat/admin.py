from django.contrib import admin
from chat.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class EventResources(resources.ModelResource):

    class Meta:
        model = Event
        list_filter = ("creater", "name", "date")
        list_display = ("creater", "invited_user", "date")


class ChatResources(resources.ModelResource):
    '''Dialogs'''
    class Meta:
        model = Chat
        list_filter = ("creater", "name", "date")



@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class= EventResources
    list_filter = ("creater", "name", "date")


@admin.register(Chat)
class ChatAdmin(ImportExportModelAdmin):
    resource_class = ChatResources
    list_display = ("room", "user", "text", "date")
    list_filter = ("room", "user", "date")


@admin.register(PrivateChat)
class PrivateChatAdmin(ImportExportModelAdmin):
    pass

@admin.register(PrivateChatMessages)
class PrivateChatMessages(ImportExportModelAdmin):
    pass
