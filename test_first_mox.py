
import unittest
import mox
import urllib2

import first


class FirstTest(unittest.TestCase):

    def setUp(self):
        #we are working with the mox module
        self.mox = mox.Mox()

        #the method we are testing will be called from this object
        self.obj = first.First()

        #stub the methods not in your layer for testing
        self.mox.StubOutClassWithMocks(urllib2, 'Request')
        self.mox.StubOutWithMock(urllib2, 'urlopen')

    def tearDown(self):
        self.mox.UnsetStubs()

    def test_get_data(self):
        request = urllib2.Request(mox.IsA(str))

        m = urllib2.urlopen(request)
        handle = self.mox.CreateMockAnything()
        m.AndReturn(handle)

        m = handle.read()
        m.AndReturn('value ni!')

        #put everything in replay mode
        self.mox.ReplayAll()
        response = self.obj.get_data('string')
        #verify, check called/expected methods
        self.mox.VerifyAll()
        self.assertEqual(response, 'value ni!')


    def test_get_data_exception(self):
        request = urllib2.Request(mox.IsA(str))

        m = urllib2.urlopen(request)
        m.AndRaise(urllib2.HTTPError('string',
                                     404,
                                     'test error 404',
                                     {},
                                     None))

        self.mox.ReplayAll()
        self.assertRaises(first.DataNotFound, self.obj.get_data,
                          'string')
        self.mox.VerifyAll()

#def main():
#    unittest.main()
#
#if __name__ == "__main__":
#    main()
