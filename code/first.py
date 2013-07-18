##first testing function##

import urllib2

class First(object):
    def get_data(self, path):

        req = urllib2.Request(path)
        response = self.urllib2.urlopen(req)
        return response.read()

    def post_data(self):
        req = urllib2.Request(norm_path, data=data)
        self.urllib2.urlopen(req)
        return True