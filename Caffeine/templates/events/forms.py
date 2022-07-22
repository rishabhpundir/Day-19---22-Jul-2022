from django import forms
from django.forms import ModelForm
from CafClubApp.models import Venue, Event

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ("venue_name", "venue_address", "phone", "web", "email", "venue_image")

        widgets = {
            "venue_name" : forms.TextInput(attrs={'class': 'form-control'}),
            "venue_address" : forms.TextInput(attrs={'class': 'form-control'}),
            "phone" : forms.TextInput(attrs={'class': 'form-control'}),
            "web" : forms.TextInput(attrs={'class': 'form-control'}),
            "email" : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ("event_name", "event_date", "venue", "manager", "attendees", "event_desc")

        labels={"event_date" : 'Date (YYYY-MM-DD HH:MM:SS) :'}

        widgets = {
            "event_name" : forms.TextInput(attrs={'class': 'form-control'}),
            "event_date" : forms.TextInput(attrs={'class': 'form-control'}),
            "venue" : forms.Select(attrs={'class': 'form-control'}),
            "manager" : forms.Select(attrs={'class': 'form-control'}),
            "attendees" : forms.SelectMultiple(attrs={'class': 'form-control'}),
            "event_desc" : forms.TextInput(attrs={'class': 'form-control'}),
        }
        