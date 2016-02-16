import os
import zipfile

from urllib import request

HOST = "http://naciscdn.org"
COUNTRIES = "/naturalearth/110m/cultural/"
COUNTRIES_FILE_NAME_NO_EXT = "ne_110m_admin_0_countries"
COUNTRIES_FILE_NAME = COUNTRIES_FILE_NAME_NO_EXT + ".zip"
FOLDER = "data/"

def _super_log(message):
    print("-" * 18)
    print(message)
    print("-" * 18 + "\n")

def _format_ogr2ogr(path='', file_name=''):
    return "ogr2ogr -f 'GeoJSON' %(path)s.geojson %(path)s/%(file_name)s.shp" % \
        { 'path': path, 'file_name': file_name }

'''
File downloadded from web

In this case it's a zip file
'''
class Webfile:
    def __init__(self, url='', file_name=''):
        self.url = url
        self.file_name = file_name

    def _already_downloaded(self):
        try:
            open(self.file_name)
            return True
        except FileNotFoundError as e:
            _super_log('Going to download file...')
            return False

    def _retreive(self):
        try:
            res = request.urlretrieve(self.url, self.file_name)
        except Exception as e:
            _super_log("Was about to retreive %s, but got error: %s" \
                      % (self.url, str(e)))
            return None

        return res

    '''
    Returns http.client.HTTPResponse

    Or None if file had been already downloadded
    '''
    def download(self):
        if self._already_downloaded():
            return None
        else:
            return self._retreive()


def process_countries():
    file_name = FOLDER + COUNTRIES_FILE_NAME

    Webfile(url=HOST + COUNTRIES + COUNTRIES_FILE_NAME,
            file_name=file_name).download()

    if not os.path.exists(file_name):
        _super_log("Can't proceed, file %s not found" % file_name)
        return 1

    # unzip zip file
    with open(file_name, 'rb') as f:
        z = zipfile.ZipFile(f)
        for name in z.namelist():
            outpath = FOLDER + COUNTRIES_FILE_NAME_NO_EXT + "/"
            z.extract(name, outpath)

    # call org2org on unzipped stuff
    path = FOLDER + COUNTRIES_FILE_NAME_NO_EXT
    os.system(_format_ogr2ogr(path=path, file_name=COUNTRIES_FILE_NAME_NO_EXT))

    # handle *.geojson file
