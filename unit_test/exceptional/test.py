import unittest
import mox

from code import first
from code import second

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
