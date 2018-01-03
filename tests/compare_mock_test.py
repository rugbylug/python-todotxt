import unittest

from todotxt.utils import ComparationMock


class CompareMockTest(unittest.TestCase):

    def test_max_compare_mock(self):
        mock = ComparationMock()
        self.assertGreater(mock, 'AAAAAAAA')
        self.assertGreaterEqual(mock, 'AAAAAAAA')
        self.assertNotEqual('AAAAAAAA', mock)
        self.assertLess('AAAAAAAA', mock)
        self.assertLessEqual('AAAAAAAA', mock)

    def test_min_compare_mock(self):
        mock = ComparationMock(always_max=False)
        self.assertGreater('AAAAAAAA', mock)
        self.assertGreaterEqual('AAAAAAAA', mock)
        self.assertNotEqual('AAAAAAAA', mock)
        self.assertLess(mock, 'AAAAAAAA')
        self.assertLessEqual(mock, 'AAAAAAAA')
