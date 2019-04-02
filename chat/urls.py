from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.EventView.as_view(), name='events'),
    path('event/<int:pk>', views.event_detail, name='event_details'),
]