import zipfile
from urllib import request
import os

HOST = "http://naciscdn.org"
COUNTRIES = "/naturalearth/110m/cultural/"
COUNTRIES_FILE_NAME_NO_EXT = "ne_110m_admin_0_countries"
COUNTRIES_FILE_NAME = COUNTRIES_FILE_NAME_NO_EXT + ".zip"
FOLDER = "data/"


'''
File downloadded from web

In this case it's a zip file
'''
class Webfile:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    '''
    Returns http.client.HTTPResponse

    Or None if file had been already downloadded
    '''
    def download(self):
        try:
            open(FOLDER + "/" + COUNTRIES_FILE_NAME)
        except:
            return request.urlretrieve(self.url, self.file_name)
        else:
            return None


def download_countries():
    # import ipdb; ipdb.set_trace()
    Webfile(HOST + COUNTRIES + COUNTRIES_FILE_NAME,
            FOLDER + '/' + COUNTRIES_FILE_NAME).download()

    # unzip zip file
    with open(FOLDER + '/' + COUNTRIES_FILE_NAME, 'rb') as f:
        z = zipfile.ZipFile(f)
        for name in z.namelist():
            outpath = FOLDER + COUNTRIES_FILE_NAME_NO_EXT + "/"
            z.extract(name, outpath)

    # call org2org on unzipped stuff
    os.system("ls -al")

    # handle *.geojson file
