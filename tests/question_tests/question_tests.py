#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_day_of_week 

class Test_Config(unittest.TestCase):

    def test_get_day_of_week(self):
        self.assertEqual('Invalid Number', get_day_of_week(0))
    def test_get_day_of_week(self):
        self.assertEqual('Monday', get_day_of_week(1))
    def test_get_day_of_week(self):
        self.assertEqual('Tuesday', get_day_of_week(2))
    def test_get_day_of_week(self):
        self.assertEqual('Wednesday', get_day_of_week(3))
    def test_get_day_of_week(self):
        self.assertEqual('Invalid Number', get_day_of_week(8))


