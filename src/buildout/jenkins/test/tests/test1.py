import unittest


class TestArithmetic(unittest.TestCase):

    def test_two_plus_two(self):
        self.assertEqual(2 + 2, 4)


def test_suite():
    return unittest.TestSuite([
        unittest.makeSuite(TestArithmetic), ])
