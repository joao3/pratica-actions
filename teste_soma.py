import unittest
from soma import soma

class TesteDaSoma(unittest.TestCase):

    def test(self):
        self.assertEqual(soma(1, 2), 3)

if __name__ == '__main__':
    unittest.main()