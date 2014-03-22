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

    def test_difference(self):
        client = APIClient()
        self.assertEqual(client.get('/difference/%d/%d' % (0, 0)), 0)
        self.assertEqual(client.get('/difference/%d/%d' % (1000, 0)), 1000)
        self.assertEqual(client.get('/difference/%d/%d' % (20, 10)), 10)

    def test_product(self):
        client = APIClient()
        self.assertEqual(client.get('/product/%d/%d' % (0, 0)), 0)
        self.assertEqual(client.get('/product/%d/%d' % (3, 2)), 6)
        self.assertEqual(client.get('/product/%d/%d' % (2, 3)), 6)

    def test_power(self):
        client = APIClient()
        self.assertEqual(client.get('/power/%d/%d' % (0, 0)), 1)
        self.assertEqual(client.get('/power/%d/%d' % (3, 2)), 9)
        self.assertEqual(client.get('/power/%d/%d' % (2, 3)), 8)



if __name__ == '__main__':
    unittest.main()
