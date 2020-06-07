import unittest

def is_prime(x):
    if x <= 0:
        print "Invalid entry!"
    elif x == 1:
        print "1 is neither prime or composite!"
    else:
        for n in range(2,x):
#if a number is divisible in x, it's NOT prime!
            if (x % n) == 0:
#return False if x is NOT prime!
                return False
        return True

class TestPrime(unittest.TestCase):
    def setUp(self):
        self.value = is_prime(51)

    def test_is_prime(self):
        self.assertTrue(is_prime(31), msg="You entered a composite number!")

    def test_is_NOT_prime(self):
        self.assertFalse(is_prime(51), msg="You entered a prime number!")
unittest.main()
