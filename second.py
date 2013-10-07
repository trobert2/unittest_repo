import first


class Second(object):

    def get_and_post(self, location, destination):
        data = first.First.get_data(location)
        first.First.post_data(destination, data)
