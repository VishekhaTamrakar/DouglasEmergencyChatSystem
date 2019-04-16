from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Say something...'
            }),
        }



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'creater', 'desc', 'is_open')


class CreatePrivateChatForm(forms.ModelForm):
    class Meta:
        model = PrivateChat
        fields = ('name', 'second_user')