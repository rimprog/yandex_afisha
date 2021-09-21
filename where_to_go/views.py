from django.shortcuts import render

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
            "placeId": place.place_id,
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json" if place.place_id=='moscow_legends' else "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json" 
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
