import unittest
from multiplica import multiplica

class TesteDoMultiplica(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplica(1, 5), 5)

if __name__ == '__main__':
    unittest.main()