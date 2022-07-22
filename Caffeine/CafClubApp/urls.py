from django.urls import path
from CafClubApp import views

urlpatterns = [
    path('', views.home, name='home_link'),
    path('venues', views.all_venues, name='venues_link'),
    path('events', views.all_events, name='events_link'),
    path('add_venue', views.add_venue, name='add_venue_link'),
    path('add_event', views.add_event, name='add_event_link'),
    path('update_venue/<venue_id>', views.update_venue, name='update_venue_link'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete_venue_link'),
]
