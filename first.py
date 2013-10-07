
import urllib2

class DataNotFound(Exception):
    pass

class First(object):
    def get_data(self, path):
        req = urllib2.Request(path)

        try:
            response = urllib2.urlopen(req)
        except Exception:
            raise DataNotFound()

        return response.read()

    def post_data(self, destination, data):
        req = urllib2.Request(destination, data=data)
        urllib2.urlopen(req)

    def read_file(self, foo):
        with open(foo, 'r') as f:
            return f.read()



#a = First()
#
#print a.read_file('file.txt')
#print a.get_data('http://example.com')
