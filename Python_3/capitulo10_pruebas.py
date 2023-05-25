import unittest
import lista

class ListaTestCase(unittest.TestCase):
    def setUp(self):
        self.li = [1, 3, 5, 7]

    def test_suma(self):
        total = lista.suma(self.li)
        self.assertEqual(total, 16)

if __name__ == '__main__':
    unittest.main()
