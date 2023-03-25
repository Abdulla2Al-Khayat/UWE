import unittest
import morse

class TestMorse(unittest.TestCase):

    def test_encode_us(self):
        self.assertEqual(morse.encode('us'), '..- ...')

    def test_decode_us(self):
        self.assertEqual(morse.decode('..- ...'), 'us')

    def test_encode_numbers(self):
        self.assertEqual(morse.encode('12345'), '.---- ..--- ...-- ....- .....')

    def test_decode_numbers(self):
        self.assertEqual(morse.decode('.---- ..--- ...-- ....- .....'), '12345')

    def test_encode_mixed(self):
        self.assertEqual(morse.encode('A1b2C3'), '.- .---- -... ..--- -.-. ...--')

    def test_decode_mixed(self):
        self.assertEqual(morse.decode('.- .---- -... ..--- -.-. ...--'), 'a1b2c3')

    # Add more test cases for various scenarios

if __name__ == '__main__':
    unittest.main()
