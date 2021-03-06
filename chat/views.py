from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import *
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from .forms import *
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.core import serializers


now=timezone.now()



@login_required
def homepage(request):
    return render(request, 'homepage.html',
                  {'dcechat': homepage})



class EventView(LoginRequiredMixin, ListView):
    template_name = "chat/events.html"
    model = Event
    context_object_name = 'events'

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Event.objects.all()
        else:
            queryset = Event.objects.filter(is_open=True)
        return queryset

class PrivateChatView(LoginRequiredMixin, ListView):
    template_name= "chat/private_chat.html"
    model = PrivateChat
    context_object_name = 'private_messages'


    def get_queryset(self):
        username = self.request.user.username
        user = self.request.user.pk
        print(user)
        if self.request.user.is_superuser:
            queryset = PrivateChat.objects.all()
        else:
            queryset = PrivateChat.objects.filter(Q(first_user=user) | Q(second_user=user)).filter(is_open=True)


        return queryset


@login_required
def private_chat_detail(request,pk):
    messages = PrivateChatMessages.objects.filter(room=pk)
    response_data = {
        'messages': messages,
        'pk':pk
    }
    return render(request, 'chat/private_chat_detail.html', response_data)


@login_required
def event_detail(request, pk):
    messages = Chat.objects.filter(room=pk)
    users = Chat.objects.filter(room=pk).values_list('user__username', flat=True).distinct()
    event_users = Event.objects.filter(id=pk)
    response_data = {
        'messages': messages,
        'pk': pk,
        'users': users
    }
    return render(request, 'chat/event_detail.html', response_data)


'''View for chat creation'''
'''received request, extends CreatePrivateCharForm to submit the request'''
@login_required
def private_chat_create(request):
    username = request.user
    if request.method == "POST":
        form = CreatePrivateChatForm(request.POST)
        if form.is_valid():
            private_chat = form.save(commit=False)
            private_chat.date = timezone.now()
            private_chat.first_user = username
            private_chat.save()
            return redirect('/private_chat')
    else:
        form = CreatePrivateChatForm()
    return render(request, 'chat/private_chat_create.html', {'form': form})

@login_required
def event_create(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = EventForm(request.POST)
            if form.is_valid():
                event = form.save(commit=False)
                event.date = timezone.now()
                event.save()
                return redirect('/events')
        else:
            form = EventForm()
        return render(request, 'chat/event_create.html', {'form': form})

# @login_required
# def create_post(request, pk):


@login_required
def create_message(request):
    if request.method == 'POST':
        '''The text from the chat'''
        post_text = request.POST.get('message')

        '''Get the Event Id from the request'''
        event_id = request.POST.get('event')
        event = Event.objects.get(id=event_id)

        '''Get the User Posting'''
        if request.user.is_authenticated:
            username = request.user.username
            print(username)

        '''Get the User Posintg'''
        user = User.objects.get(username=username)

        '''Create new chat message'''
        message = Chat.objects.create(room=event,user=user, text=post_text)
        message.save() #this saves the message


        '''This is the response data'''
        response_data = {}
        response_data['result'] = 'Create post successful!'
        response_data['messagepk'] = message.pk
        response_data['text'] = message.text
        response_data['date'] = message.date
        response_data['user'] = username

        return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")
    else:
        data1 = "bad response"
        return HttpResponse(json.dumps(data1), content_type="application/json")


@login_required
def create_private_message(request):
    if request.method == 'POST':
        '''The text from the Chat'''
        post_text = request.POST.get('message')
        print(post_text)

        '''Get the private chat ID from request'''
        chat_id = request.POST.get('chat_id')
        chat = PrivateChat.objects.get(id=chat_id)

        '''User who is posting a message'''
        if request.user.is_authenticated:
            username = request.user.username

        '''Get the user'''
        user = User.objects.get(username=username)


        '''Create new chat message'''
        message = PrivateChatMessages.objects.create(room=chat,user=user, text=post_text)
        message.save()

        '''This is the response data'''
        response_data = {}
        response_data['result'] = 'Message was successfully posted'
        # response_data['messagepk'] = message.pk
        # response_data['text'] = message.text
        # response_data['date'] = message.date
        # response_data['user'] = username

        return HttpResponse(json.dumps(response_data, cls=DjangoJSONEncoder), content_type="application/json")
    else:
        data = 'Error please check'
        return HttpResponse(json.dumps(data), content_type="application/json")



@login_required
def active_users_for_event(request):
    event = request.GET.get('event')
    print(event)
    users = Event.objects.filter(id=event)
    data = serializers.serialize('json', users, fields=('invited'))

    print(users)
    return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")



@login_required
def private_chat_edit(request, pk):
    private_chat = get_object_or_404(PrivateChat, pk=pk)
    if request.method == "POST":
        form = UpdatePrivateChatForm(request.POST, instance=private_chat)
        if form.is_valid():
            private_chat = form.save(commit=False)
            private_chat.date = timezone.now()
            private_chat.save()
            return redirect('/private_chat')
    else:
        form = UpdatePrivateChatForm(instance=private_chat)
        return render(request, 'chat/private_chat_edit.html', {'form': form})

@login_required
def event_edit(request, pk):
    if request.user.is_superuser:
        event = get_object_or_404(Event, pk=pk)
        if request.method == "POST":
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                event = form.save(commit=False)
                event.date = timezone.now()
                event.save()
                # return render(request, 'chat/events.html', {'events': event})
                return redirect('/events')
        else:
            form = EventForm(instance=event)
            return render(request, 'chat/event_edit.html', {'form': form})



@login_required
def private_chat_delete(request, pk):
    if request.user.is_superuser:
        private_chat = get_object_or_404(PrivateChat, pk=pk)
        private_chat.delete()
        return redirect('/private_chat')

@login_required
def event_delete(request, pk):
    if request.user.is_superuser:
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        return redirect('/events')