import mock
import unittest
import second

class TestSecond(unittest.TestCase):
    def setUp(self):
        self.obj = second.Second()

    @mock.patch('first.First.get_data')
    @mock.patch('first.First.post_data')
    def test_get_and_post(self, mock_post_data, mock_get_data):
        mock_get_data.return_value = 'data'
        self.obj.get_and_post("loc", "dest")
        mock_get_data.assert_called_with('loc')
        mock_post_data.assert_called_with('dest', 'data')