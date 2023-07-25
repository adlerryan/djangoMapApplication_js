from django.db import models
from django.conf import settings
from urllib.parse import urljoin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class LocationType(models.Model):
    TYPES = (
        ('bar', 'Bar'),
        ('brewery', 'Brewery'),
        ('club', 'Club'),
        ('winebar', 'Wine Bar'),
        ('restaurant', 'Restaurant')
        # Add more types as needed
    )
    name = models.CharField(max_length=10, choices=TYPES)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MaxValueValidator(10.0)])  # e.g. 4.5
    lat = models.DecimalField(max_digits=25, decimal_places=6)  # Latitude
    lng = models.DecimalField(max_digits=25, decimal_places=6)  # Longitude
    cover_charge = models.BooleanField(default=False)  # e.g. 10.00
    url = models.URLField(max_length=200, blank=True, null=True)  # URL field

    # New fields
    address = models.TextField()
    location_type = models.ManyToManyField(LocationType)
    phone_number = models.CharField(max_length=20) # Adjust length based on possible international numbers
    tags = models.ManyToManyField('Tag', related_name='locations')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class LocationImage(models.Model):
    location = models.ForeignKey(Location, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='location_images/')
    featured = models.BooleanField(default=False)
    
    def image_url(self):
        return urljoin(settings.MEDIA_URL, self.image.url) if self.image and hasattr(self.image, 'url') else ''

class Review(models.Model):
    location = models.ForeignKey(Location, related_name='reviews', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"{self.location.name} Review"

class MenuItem(models.Model):
    location = models.ForeignKey(Location, related_name='menu_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# Affiliate App Model
class AffiliateApp(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Affiliate App URL Model
class AffiliateAppURL(models.Model):
    location = models.ForeignKey(Location, related_name='affiliate_urls', on_delete=models.CASCADE)
    app = models.ForeignKey(AffiliateApp, related_name='urls', on_delete=models.CASCADE)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.app.name} URL for {self.location.name}"
