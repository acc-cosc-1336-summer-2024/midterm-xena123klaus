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

from src.question_b.question_b import get_person_category

class Test_Config(unittest.TestCase):
    def test_get_person_category(self):
        self.assertEqual('infant' , get_person_category(1))
    def test_get_person_category(self):
        self.assertEqual('child' , get_person_category(2))
    def test_get_person_category(self):
        self.assertEqual('teenager' , get_person_category(14))
    def test_get_person_category(self):
        self.assertEqual('adult' , get_person_category(20))


from src.question_c.question_c import is_prime

class Test_Config(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(False , is_prime(4))
    def test_is_prime(self):
        self.assertEqual(True , is_prime(5))
    def test_is_prime(self):
        self.assertEqual(True , is_prime(11))


    
