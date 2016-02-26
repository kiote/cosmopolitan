import os
import json

from cosmopolitan.models import Country
from cosmopolitan.models import City
from cosmopolitan.models import Polygon

import cosmopolitan.management.commands.service.common as common

# countrise data URL
# http://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip

COUNTRIES = {
                "file_name_without_extension": "ne_10m_admin_0_countries",
                "file_name": "ne_10m_admin_0_countries.zip",
            }

def process_countries():
    data = common.prepare_data(COUNTRIES)

    print("\n--- Seeding countries: ---")

    Polygon.objects.filter(type='country').delete()

    for feature in data["features"]:
        json_country_code = feature["properties"]["ISO_A2"]
        try:
            country = Country.objects.get(pk=json_country_code.lower())
        except Country.DoesNotExist:
            print('Not found: ' + json_country_code, end='')

        country_polygon = Polygon(id="%s:%s" % ("country", country.id))
        country_polygon.type = "country"
        country_polygon.type_id = country.id
        country_polygon.polygon = json.dumps(feature["geometry"]["coordinates"])
        country_polygon.save()

        print(".", end="", flush=True)

    print("\nFinish.")

CITIES = {
            "file_name_without_extension": "ne_10m_populated_places",
            "file_name": "ne_10m_populated_places.zip",
         }

def process_cities():
    data = common.prepare_data(CITIES)

    print("\n--- Seeding cities: ---")

    Polygon.objects.filter(type='city').delete()

    for feature in data["features"]:
        json_city_name = feature["properties"]["GN_ASCII"]
        try:
            if json_city_name is None:
                continue
            city = City.objects.get(name=json_city_name)
            city_polygon = Polygon(id="%s:%s" % ("city", city.id))
            city_polygon.type = "city"
            city_polygon.type_id = city.id
            city_polygon.polygon = json.dumps(feature["geometry"]["coordinates"])
            city_polygon.save()
            print(".", end="", flush=True)
        except City.DoesNotExist:
            pass

    print("\nFinish.")