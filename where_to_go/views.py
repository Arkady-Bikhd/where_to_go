from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def init_place_params(place):
    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [place.longitude, place.latitude]
        },
        'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': reverse('places', args=[place.id])
        },
    }


def show_index_page(request):
    places = Place.objects.all()
    context = {
        'places_info': {
            'type': 'FeatureCollection',
            'features': [init_place_params(place) for place in places]
        }

    }    
    return render(request, 'index.html', context)


def upload_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_info = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        }
    }
    return JsonResponse(
        place_info,
        json_dumps_params={'ensure_ascii': False}
    )
