#!/usr/bin/python3
"""
Defines views for the Place resource
"""

from flask import jsonify, request, abort
from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def places_search():
    """
    Retrieve all Place objects depending on the JSON in the body of the request.
    """
    if not request.json:
        abort(400, description="Not a JSON")

    search_criteria = request.get_json()
    if not search_criteria:
        places = storage.all(Place).values()
        return jsonify([place.to_dict() for place in places])

    states_ids = search_criteria.get('states', [])
    cities_ids = search_criteria.get('cities', [])
    amenities_ids = search_criteria.get('amenities', [])

    places_set = set()

    if states_ids:
        for state_id in states_ids:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    for place in city.places:
                        places_set.add(place)

    if cities_ids:
        for city_id in cities_ids:
            city = storage.get(City, city_id)
            if city:
                for place in city.places:
                    places_set.add(place)

    if not states_ids and not cities_ids:
        places_set = set(storage.all(Place).values())

    if amenities_ids:
        amenities_set = set(amenities_ids)
        filtered_places = set()
        for place in places_set:
            place_amenities_ids = {amenity.id for amenity in place.amenities}
            if amenities_set.issubset(place_amenities_ids):
                filtered_places.add(place)
        places_set = filtered_places

    return jsonify([place.to_dict() for place in places_set])

