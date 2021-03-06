from urllib import request

import cosmopolitan.management.commands.service.os as sos


class Webfile(object):
    """
    File downloaded from web

    In this case it's a zip file
    """
    def __init__(self, url='', file_name=''):
        self.url = url
        self.file_name = file_name

    def _already_downloaded(self):
        try:
            open(self.file_name)
            return True
        except FileNotFoundError as e:
            sos._super_log('Downloading the file...')
            return False

    def _retreive(self):
        try:
            res = request.urlretrieve(self.url, self.file_name)
        except Exception as e:
            sos._super_log("Was about to retreive %s, but got error: %s"
                           % (self.url, str(e)))
            return None

        return res

    """
    Returns http.client.HTTPResponse

    Or None if file had been already downloadded
    """
    def download(self):
        if self._already_downloaded():
            return None
        else:
            return self._retreive()
