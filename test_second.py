
import unittest
import mox

import first
import second


class FirstTest(unittest.TestCase):

    def setUp(self):
        self.fake_location = 'http://fake.example.example.net.org.com'
        self.fake_destination = 'http://fake.com/post_location'
        self.fake_data = 'fake_data'

        self.obj = second.Second()

        self.mox = mox.Mox()
        self.mox.StubOutWithMock(first.First, 'get_data')
        self.mox.StubOutWithMock(first.First, 'post_data')

    def tearDown(self):
        self.mox.UnsetStubs()

    def test_post_and_get(self):
        m = first.First.get_data(self.fake_location)
        m.AndReturn(self.fake_data)

        first.First.post_data(self.fake_destination, self.fake_data)

        self.mox.ReplayAll()
        response = self.obj.get_and_post(self.fake_location,
                                         self.fake_destination)
        self.mox.VerifyAll()

        self.assertEqual(response, None)
