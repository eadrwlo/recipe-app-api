"""
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ Test te calc module """
    def test_add(self):
        res = calc.add(5, 5)
        self.assertEqual(res, 10)



