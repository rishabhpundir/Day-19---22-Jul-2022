from django.contrib import admin
from CafClubApp.models import Venue, CaffeineUser, Event

# Register your models here.
admin.site.register(CaffeineUser)
# admin.site.register(Venue)
admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'venue_address', 'phone')
    ordering = ('venue_name',)
    search_fields = ('venue_name', 'venue_address')