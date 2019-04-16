from django.db import models
from django.contrib.auth.models import User


'''Chat Models such as Event and Chat'''
class Event(models.Model):
    '''Event Room'''
    name = models.CharField(max_length=100)
    creater = models.ForeignKey(User, verbose_name="Creater", on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, blank=True, null=True)
    invited = models.ManyToManyField(User, verbose_name="Participants", related_name="invited_user", blank=True, null=True)
    date = models.DateTimeField("Date Created", auto_now_add=True)
    is_open = models.BooleanField(default=True, blank=False, null=False)


    class Meta:
        verbose_name="Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.name


class Chat(models.Model):
    '''Chat Messages'''
    room = models.ForeignKey(Event, verbose_name="Event Room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Date Sent", auto_now_add=True)


    class Meta:
        verbose_name="Chat Message"
        verbose_name_plural="Chat Messages"

    def __str__(self):
        return str(self.room)


'''Private Message'''
class PrivateChat(models.Model):
    name = models.CharField(max_length=100)
    first_user = models.ForeignKey(User, verbose_name="First User", on_delete=models.CASCADE, related_name='chat_first_user')
    second_user = models.ForeignKey(User, verbose_name="Second User", on_delete=models.CASCADE, related_name='chat_second_user')
    is_open = models.BooleanField(default=True, blank=False, null=False)

    class Meta:
        verbose_name="Private Chat Room"
        verbose_name_plural = "Private Chat Rooms"

    def __str__(self):
        return str(self.name)

'''Private Chat Messages'''
class PrivateChatMessages(models.Model):
    room = models.ForeignKey(PrivateChat, verbose_name="Private Chat Room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Date Sent", auto_now_add=True)

    class Meta:
        verbose_name="Private Chat Message"
        verbose_name_plural="Private Chat Messages"


    def __str__(self):
        return self.name
