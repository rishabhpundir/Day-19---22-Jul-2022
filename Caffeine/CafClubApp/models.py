from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CaffeineUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField('User Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Venue(models.Model):
    venue_name = models.CharField('Venue Name', max_length=120)
    venue_address = models.CharField(max_length=120)
    phone = models.CharField('Contact Phone No.',max_length=120)
    web = models.URLField('Website Address', null=True, blank=True)
    email = models.EmailField('Email Address')
    venue_image = models.ImageField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return self.venue_name

class Event(models.Model):
    event_name = models.CharField('Event Name', max_length=50)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    event_desc = models.CharField('Event Description', max_length=200, blank=True)
    attendees = models.ManyToManyField(CaffeineUser, blank=True)

    def __str__(self):
        return self.event_name

    