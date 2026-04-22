import unittest
from mean_var_std import calculate


class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[9.555555555555557, 0.6666666666
