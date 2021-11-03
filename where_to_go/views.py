from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from places.models import Place


def create_geo_json(places):
    geo_json_points = []

    for place in places:
        geo_json_point = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl":  reverse('place_details', kwargs={'place_id': place.id})
            }
        }

        geo_json_points.append(geo_json_point)

    geo_json = {
        "type": "FeatureCollection",
        "features": geo_json_points
    }

    return geo_json


def show_index_page(request):
    places = Place.objects.all()
    geo_json = create_geo_json(places)

    return render(request, 'index.html', context={'geo_json':geo_json})


def get_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_details = {
        "title": place.title,
        "imgs": [place_image.image.url for place_image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude
        }
    }

    response = JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )

    return response
