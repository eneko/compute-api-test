import unittest
from api import APIClient


class TestMath(unittest.TestCase):

    def test_sum(self):
        client = APIClient()
        self.assertEqual(client.get('/sum/%d/%d' % (0, 0)), 0)
        self.assertEqual(client.get('/sum/%d/%d' % (0, 1)), 1)
        self.assertEqual(client.get('/sum/%d/%d' % (0, 1000)), 1000)
        self.assertEqual(client.get('/sum/%d/%d' % (0, 1234567890)), 1234567890)
        self.assertEqual(client.get('/sum/%d/%d' % (0, 1111222233334444555566667777888899990000)), 1111222233334444555566667777888899990000)
        self.assertEqual(client.get('/sum/%d/%d' % (1, 1)), 2)
        self.assertEqual(client.get('/sum/%d/%d' % (434208821908, 432838921)), 434641660829)
        self.assertEqual(client.get('/sum/%d/%d' % (0, -0)), -0)
        self.assertEqual(client.get('/sum/%d/%d' % (0, -1)), -1)
        self.assertEqual(client.get('/sum/%d/%d' % (0, -1000)), -1000)
        self.assertEqual(client.get('/sum/%d/%d' % (0, -1234567890)), -1234567890)
        self.assertEqual(client.get('/sum/%d/%d' % (0, -1111222233334444555566667777888899990000)), -1111222233334444555566667777888899990000)
        self.assertEqual(client.get('/sum/%d/%d' % (1, -1)), 0)
        self.assertEqual(client.get('/sum/%d/%d' % (434208821908, -432838921)), 433775982987)
        self.assertEqual(client.get('/sum/%d/%d' % (-0, -0)), -0)
        self.assertEqual(client.get('/sum/%d/%d' % (-0, -1)), -1)
        self.assertEqual(client.get('/sum/%d/%d' % (-0, -1000)), -1000)
        self.assertEqual(client.get('/sum/%d/%d' % (-0, -1234567890)), -1234567890)
        self.assertEqual(client.get('/sum/%d/%d' % (-0, -1111222233334444555566667777888899990000)), -1111222233334444555566667777888899990000)
        self.assertEqual(client.get('/sum/%d/%d' % (-1, -1)), -2)
        self.assertEqual(client.get('/sum/%d/%d' % (-434208821908, -432838921)), -434641660829)

if __name__ == '__main__':
    unittest.main()
