from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place



def place_params(place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.latitude, place.longitude]
            },
        "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse('places', args=[place.id])
            },
        }


def show_index_page(request):

    places = Place.objects.all()
    context = {
        "places_info": {
            "type": "FeatureCollection",
            "features": [place_params(place) for place in places]
            }

        }
    
    return render(request, 'index.html', context)


def places(request, place_id):

    place = get_object_or_404(Place, pk=int(place_id))
    place_info = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all().order_by('image_number')],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        }
    }
    responce = JsonResponse(
        place_info,        
        json_dumps_params={'ensure_ascii': False}
        )

    return responce
