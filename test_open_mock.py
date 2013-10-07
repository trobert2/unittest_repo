
import unittest
import mock
import first

class OpenTest(unittest.TestCase):

    def setUp(self):
        self.obj = first.First()

    def test_open(self):
        with mock.patch('first.open', mock.mock_open(
            read_data='fake_data'), create=True):

                response = self.obj.read_file('fake.txt')

                self.assertEqual(response, 'fake_data')
                print 'this is the data ' + response
