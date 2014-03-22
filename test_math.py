import unittest
from api import APIClient


class TestMath(unittest.TestCase):

    def test_sum(self):
        client = APIClient()
        self.assertEqual(client.get('/sum/%d/%d' % (0, 0)), 0)

if __name__ == '__main__':
    unittest.main()
