import os

from cosmopolitan.models import Country

import cosmopolitan.management.commands.service.web as sweb
import cosmopolitan.management.commands.service.os as sos

# countrise data URL
# http://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip

HOST = "http://naciscdn.org"
FOLDER = "data/"

COUNTRIES = {
                "http_path": "/naturalearth/10m/cultural/",
                "file_name_without_extension": "ne_10m_admin_0_countries",
                "file_name": "ne_10m_admin_0_countries.zip",
            }

def process_countries():
    file_name = FOLDER + COUNTRIES["file_name"]

    sweb.Webfile(url=HOST + COUNTRIES["http_path"] + COUNTRIES["file_name"],
                 file_name=file_name).download()

    if not os.path.exists(file_name):
        sos._super_log("Can't proceed, file %s not found" % file_name)
        return 1

    # unzip zip file
    outpath = FOLDER + COUNTRIES["file_name_without_extension"] + "/"
    sos.Unzip(file_name=file_name, outpath=outpath).run()

    # call org2org on unzipped stuff
    sos._format_ogr2ogr(path=FOLDER + COUNTRIES["file_name_without_extension"],
                        file_name=COUNTRIES["file_name_without_extension"])

    # handle *.geojson file
    data = sos.LoadGeoJSON(FOLDER + COUNTRIES["file_name_without_extension"]).run()

    print("\n--- Seeding countries: ---")

    for feature in data["features"]:
        json_country_code = feature["properties"]["ISO_A2"]
        try:
            country = Country.objects.get(pk=json_country_code.lower())
        except Country.DoesNotExist:
            print('Not found: ' + json_country_code, end='')
            # country = Country.objects.get(name=mappings[json_country_name])

        country.polygon = feature["geometry"]["coordinates"]
        country.save()

        print(".", end="", flush=True)
