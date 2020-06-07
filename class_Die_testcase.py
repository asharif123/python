from class_dice import Die
import unittest
import random

class TestDie(unittest.TestCase):

    def setUp(self):
        self.roll = Die(20)
        self.numbers_list = range(1,self.roll.sides+1)
        self.random_value = random.randint(1,self.roll.sides)
        
        
    def test_roll_die(self):      
        #print numbers
        self.assertEqual(self.roll.sides,20)

    def test_random_value(self):
        self.assertIn(self.random_value,self.numbers_list)
unittest.main()
