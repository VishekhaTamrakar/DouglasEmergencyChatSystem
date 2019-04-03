from django.urls import path,include,re_path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.EventView.as_view(), name='events'),
    path('event/<int:pk>', views.event_detail, name='event_details'),
    path('post_message', views.create_message, name='message_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/create', views.event_create, name='event_create'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
]