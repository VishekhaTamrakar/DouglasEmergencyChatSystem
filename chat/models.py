from django.db import models
from django.contrib.auth.models import User


'''Chat Models such as Event and Chat'''
class Event(models.Model):
    '''Event Room'''
    creater = models.ForeignKey(User, verbose_name="Creater", on_delete=models.CASCADE)
    invited = models.ManyToManyField(User, verbose_name="Participants", related_name="invited_user")
    date = models.DateTimeField("Date Created", auto_now_add=True)


    class Meta:
        verbose_name="Event"
        verbose_name_plural = "Events"


class Chat(models.Model):
    '''Chat Messages'''
    room = models.ForeignKey(Event, verbose_name="Event Room", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    text = models.TextField("Message", max_length=500)
    date = models.DateTimeField("Date Sent", auto_now_add=True)


    class Meta:
        verbose_name="Chat Message"
        verbose_name_plural="Chat Messages"

