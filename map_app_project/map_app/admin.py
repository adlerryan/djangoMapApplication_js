from django.contrib import admin
from .models import (
    Location, 
    LocationImage, 
    Review, 
    MenuItem, 
    Tag, 
    LocationType,  # Import LocationType here
    AffiliateApp, 
    AffiliateAppURL  # Import new models here
)

class LocationImageInline(admin.TabularInline):
    model = LocationImage
    extra = 0

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0

class AffiliateAppURLInline(admin.TabularInline):  # New InlineModelAdmin for AffiliateAppURL
    model = AffiliateAppURL
    extra = 0

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'rating', 'lat', 'lng', 'cover_charge', 'url']  # Add 'url' here
    inlines = [LocationImageInline, ReviewInline, MenuItemInline, AffiliateAppURLInline]  # Add AffiliateAppURLInline here
    filter_horizontal = ('tags', 'location_type',)  # Add 'location_type' here

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(LocationType)  # Register LocationType with the admin interface
class LocationTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(AffiliateApp)  # Register AffiliateApp with the admin interface
class AffiliateAppAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

# You don't need to register AffiliateAppURL separately, 
# as it's already included as an inline in the Location admin interface
