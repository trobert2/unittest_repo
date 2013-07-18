##first testing function##

import urllib2

class DataNotFound(Exception):
    pass

class First(object):
    def get_data(self, path):

        req = urllib2.Request(path)
        try:
            response = self.urllib2.urlopen(req)
        except urllib2.HTTPError() as ex:
                if ex.code == 404:
                    raise DataNotFound()
                else:
                    raise

        return response.read()

    def post_data(self, destination, data):
        req = urllib2.Request(destination, data=data)
        self.urllib2.urlopen(req)
        return True