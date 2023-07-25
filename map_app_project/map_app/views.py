from django.shortcuts import render, redirect
from .models import Location
import json
from django.conf import settings

def main_page(request):
    locations = Location.objects.all()
    locations_list = []
    for location in locations:
        # Adjust here to prepend the domain and protocol to the image URL
        images = [request.build_absolute_uri(image.image_url()) for image in location.images.all()]
        print(images)
        location_dict = {
            'model': 'map_app.location',
            'pk': location.pk,
            'fields': {
                'name': location.name,
                'lat': str(location.lat),
                'lng': str(location.lng),
                'rating': str(location.rating),
                'address': location.address,
                'images': images,
            },
        }
        locations_list.append(location_dict)
    locations_json = json.dumps(locations_list)
    context = {'locations': locations_json}
    return render(request, 'map_app/main_page.html', context)
