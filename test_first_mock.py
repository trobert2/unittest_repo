
import unittest
import mock
import urllib2

import first


class FirstTest(unittest.TestCase):

    def setUp(self):
        #the method we are testing will be called from this object
        self.obj = first.First()


    def test_get_data(self):
        path = 'http://example.com'
        text = ' random text'
        urllib2.Request = mock.MagicMock()

        handle = mock.Mock()
        urllib2.urlopen = mock.MagicMock(return_value=handle)

        handle.read.return_value = text

############## the method we are testing ##########
        response = self.obj.get_data(path)
###################################################

        urllib2.urlopen.assert_called_with(urllib2.Request())
        handle.read.assert_called_once_with()
        self.assertEqual(response, text)

#def main():
#    unittest.main()
#
#if __name__ == "__main__":
#    main()
