from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html',
                  {'dcechat': homepage})



class EventView(ListView):
    template_name = "chat/events.html"
    model = Event
    context_object_name = 'events'


@login_required
def event_detail(request, pk):
    messages = Chat.objects.filter(room=pk)
    return render(request, 'chat/event_detail.html', {'messages':messages})

# @login_required
# def create_post(request, pk):


