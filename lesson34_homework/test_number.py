import unittest

from number import Number


class TestNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.num = Number(22)
        self.num_0 = Number(0)
        self.num_1 = Number(-15)

    def test_number(self):
        self.num.number = '1.1'
        self.assertNotEqual('1.1', self.num.number, 'Value not integers')
        self.num.number = 11
        self.assertEqual(11, self.num.number, 'Value integers')

    def test_number_to_oct(self):
        self.assertEqual('0o26', self.num.number_to_oct, f'Incorrect translation into octal number system')
        self.assertEqual('0o0', self.num_0.number_to_oct, f'Incorrect translation into octal number system')
        self.assertEqual('0o', self.num_1.number_to_oct, f'Incorrect translation into octal number system')

    def test_number_to_hex(self):
        self.assertEqual('0x16', self.num.number_to_hex, f'Incorrect translation into hexadecimal number system')
        self.assertEqual('0x0', self.num_0.number_to_hex, f'Incorrect translation into hexadecimal number system')
        self.assertEqual('0x', self.num_1.number_to_hex, f'Incorrect translation into hexadecimal number system')

    def test_number_to_bin(self):
        self.assertEqual('0b10110', self.num.number_to_bin, f'Incorrect translation into binary number system')
        self.assertEqual('0b0', self.num_0.number_to_bin, f'Incorrect translation into binary number system')
        self.assertEqual('0b', self.num_1.number_to_bin, f'Incorrect translation into binary number system')


if __name__ == '__main__':
    unittest.main()
