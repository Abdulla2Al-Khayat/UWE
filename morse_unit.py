import unittest
import morse

class TestMorse(unittest.TestCase):

    def test_encode_us(self):
        self.assertEqual(morse.encode('us'), '..- ...')

    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'), 'us')

    # Add more test cases for various scenarios

if __name__ == '__main__':
    unittest.main()
