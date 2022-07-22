from wsgiref.util import request_uri
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Event, Venue
from templates.events.forms import EventForm, VenueForm

# Create your views here.
def home(request):
    return render(request, 'events/home.html')

def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/events_list.html', context={'events':events})

def all_venues(request):
    venues = Venue.objects.all()
    return render(request, 'events/venues.html', context={'venues':venues})

def add_venue(request):
    submitted = False
    form = VenueForm
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form':form, 'submitted': submitted})

def add_event(request):
    submitted = False
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {'form':form, 'submitted': submitted})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect('/venues')
    return render(request, 'events/update_venue.html', context={'form':form, 'venue':venue})

#Delete a venue
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return HttpResponseRedirect('/venues')
