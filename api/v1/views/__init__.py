#!/usr/bin/python3
"""Initialize Flask Blueprint object for API v1."""
from flask import Blueprint
from os import getenv

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views from the directory
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from api.v1.views.index import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.amenities import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.places_amenities import *  # Import places_amenities module
else:
    from api.v1.views.index import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.amenities import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.places_amenities import *  # Import places_amenities module

