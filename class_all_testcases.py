#####testcase examples

##testcase to reverse a list
##Example: reverseList([1,3,5,6]) should return [6,5,3,1]
##USE SWAPPING!
import unittest
def reverse_list(arr):
    length = int(len(arr)/2)
    for i in range(length):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
    return arr

##return true if palindrome exists

def is_palindrome(word):
    reverse_word = ''
    for i in range(len(word)-1,-1,-1):
        reverse_word += word[i]
    if reverse_word == word:
        return True

##return the change in quarters,dimes,nickels,pennies

def coins(change):

    change_list = []

    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    if change > 25:
        quarters = change // 25
        change -= (quarter*quarters)
    else:
        quarters = 0
    change_list.append(quarters)

    if change > dime:
        dimes = change // dime
        change -= (dime*dimes)
    else:
        dimes = 0
    change_list.append(dimes)

    if change > nickel:
        nickels = change // nickel
        change -= (nickel*nickels)
    else:
        nickels = 0
    change_list.append(nickels)

    if change > penny:
        pennies = change // penny
        change -= (penny*pennies)
    else:
        pennies = 0
    change_list.append(pennies)
        
    return change_list
print(coins(187))

##factorial

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

##fibonacci
    
def fib(num):
    if num == 1:
        return 0

    elif num == 2:
        return 1

    else:
        return fib(num-1) + fib(num-2)
    

class TestReverse(unittest.TestCase):

    def test_is_reversed_short_list(self):
        self.assertEqual((reverse_list([6,5,3,1])),[1,3,5,6])   

    def test_not_equal(self):
        #verify that the array gets reversed and dont get same array!
        self.assertNotEqual((reverse_list([1,3,5])),[1,3,5])

    def test_is_reversed_long_list(self):
        self.assertEqual(reverse_list([1,2,3,4,5,6,7,8,9]),[9,8,7,6,5,4,3,2,1])

    def setUp(self):
        print("Executing testcase...", self)

    def tearDown(self):
        print("Testcase completed\n")

class TestPalindrome(unittest.TestCase):

    def test_is_equal(self):
        self.assertEqual(is_palindrome('racecar'),True)

    def test_is_true(self):
        self.assertTrue(is_palindrome('radar'))

    def test_is_false(self):
        self.assertFalse(is_palindrome('radars'))

    def test_not_equal(self):
        self.assertNotEqual(is_palindrome('Madam'),True)

    def test_assert_is(self):
        self.assertIs(is_palindrome('madam'),True)


    def setUp(self):
        print("Executing testcase...", self)

    def tearDown(self):
        print("Testcase completed\n")

class Testcoins(unittest.TestCase):
    
    def test_change(self):
        self.assertEqual(coins(87),[3,1,0,2])
        self.assertEqual(coins(102),[4,0,0,2])
        self.assertEqual(coins(7),[0,0,1,2])
        self.assertEqual(coins(19),[0,1,1,4])
        self.assertEqual(coins(187),[7,1,0,2])
        

    def setUp(self):
        print("running testcase...", self)

    def tearDown(self):
        print("testcase completed\n", self)

class TestFactorial(unittest.TestCase):

    def test_factorial_is_equal(self):
        self.assertEqual(factorial(5),120)
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(4),24)
        self.assertEqual(factorial(6),720)

    def setUp(self):
        print("running testcase...", self)

    def tearDown(self):
        print("testcase completed\n", self)

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_is_equal(self):

        self.assertEqual(fib(5),3)
        self.assertEqual(fib(1),0)
        self.assertEqual(fib(2),1)
        self.assertEqual(fib(9),21)
        self.assertEqual(fib(8),13)

    def setUp(self):
        print("running testcase...", self)

    def tearDown(self):
        print("testcase completed\n", self)

if __name__ == '__main__':
    unittest.main()





