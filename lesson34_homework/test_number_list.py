import unittest

from number_list import NumberList


class TestNumberList(unittest.TestCase):
    def setUp(self) -> None:
        self.num_list = NumberList()

    def test_update_numbers_list(self):
        self.assertNotEqual(self.num_list, self.num_list.update_numbers_list())

    def test_get_sum(self):
        num_sum = sum(*self.num_list.__dict__.values())
        self.assertEqual(num_sum, self.num_list.get_sum())
        self.num_list.update_numbers_list()
        self.assertNotEqual(num_sum, self.num_list.get_sum())

    def test_get_arg(self):
        num_avg = sum(*self.num_list.__dict__.values()) / len(*self.num_list.__dict__.values())
        self.assertEqual( num_avg, self.num_list.get_avg())
        self.num_list.update_numbers_list()
        self.assertNotEqual(num_avg, self.num_list.get_avg())

    def test_get_max(self):
        num_max = max(*self.num_list.__dict__.values())
        self.assertEqual(num_max, self.num_list.get_max())
        self.num_list.update_numbers_list()
        self.assertNotEqual(num_max, self.num_list.get_max())

    def test_get_min(self):
        num_min = min(*self.num_list.__dict__.values())
        self.assertEqual(num_min, self.num_list.get_min())
        self.num_list.update_numbers_list()
        self.assertNotEqual(num_min, self.num_list.get_min())


if __name__ == '__main__':
    unittest.main()
