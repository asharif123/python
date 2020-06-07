import unittest

class MathDojo:
    def __init__(self):
        self.result = 0
        
    def add(self,num,*nums):
        self.result += num
      #  print(self.result)
        for value in nums:
            self.result += value
        return self

    def subtract(self,num,*nums):
        self.result -= num
        for num in nums:
            self.result -= num
        return self

    
##creating instance of MathDojo class
testing = MathDojo()

class TestMathDojo(unittest.TestCase):

    
    def setUp(self):
        print("Starting test...", self)

    def test_addition(self):
        addition = testing.add(4,8,15,16,23,42)
        self.assertEqual(addition.result,108)

    def test_subtraction(self):
        subtraction = testing.subtract(21,31,41)
        self.assertEqual(subtraction.result,15)        

    def tearDown(self):
        print("Testcases completed\n")

if __name__ == "__main__":
    unittest.main()

    
