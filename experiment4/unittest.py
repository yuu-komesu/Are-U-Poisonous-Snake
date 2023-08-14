import unittest

from fine_chuning_vgg16 import conclete


class Testconclete(unittest.TestCase):
    """test class of fine_chuning_vgg16
    """
    
    def test_conclete(self):
        value1 = 20
        expected = 14, 4, 2
        actual = conclete(value1)
        self.assertEqual(expected, actual)
        

if __name__ == "__main__":
    unittest.main()
