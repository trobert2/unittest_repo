import unittest
import mox

from code.exceptional import first
from code.exceptional import second

class ExceptionalTest(unittest.TestCase):

    def setUp(self):
        self.mox = mox.Mox()

    def tearDown(self):
        self.mox.UnsetStubs()



    def test_post_and_get(self):
        pass

    def test_post_and_get_exception(self):
        pass