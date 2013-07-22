import unittest
import mox
import urllib2

from code.exceptional import first
from code.exceptional import second

class ExceptionalTest(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()
        self.mox.StubOutWithMock(first.First,'get_data')
        self.mox.StubOutWithMock(first.First,'post_data')
        self.fake_json={'fake_json':'fake_data'}
        self.source='http://www.example.com/login.html'
        self.destination=self.source
        
    def tearDown(self):
        self.mox.UnsetStubs()

    def test_post_and_get(self):
        obiect=second.Second()
        m=first.First.get_data(mox.IsA(str))
        m.AndReturn(self.fake_json)
        m=first.First.post_data(mox.IsA(str),self.fake_json)
        m.AndReturn(True)
        self.mox.ReplayAll()
        response=obiect.get_and_post(self.source,self.destination)
        self.mox.VerifyAll()
        self.assertTrue(response)
        
    def test_post_and_get_exception(self): 
        obiect=second.Second()
        m=first.First.get_data(self.source)
        m.AndRaise(first.DataNotFound())
        self.mox.ReplayAll()
        self.assertRaises(first.DataNotFound,
                        obiect.get_and_post, self.source, self.destination) 
        self.mox.VerifyAll()
