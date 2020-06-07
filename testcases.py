import unittest

#import 'get_formatted_name' function from 'test_name_function' script
from test_name_function import get_formatted_name
#since we are testing the 'get_formatted_name' function!!
##from test_name_function import get_formatted_name
##
#class creates a series of unittests for NameTestCase class
#class name should have test in it and what func you're testing!
class NameTestCase(unittest.TestCase):
#test the get_formatted_name function from the test_name_function script
#test to see if name is outputted correctly!
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Awad','Sharif')
#confirms that the formatted_name is equal to expected 'Awad Sharif'
        self.assertEqual(formatted_name, 'Awad Sharif')

    def test_first_middle_last_name(self):
        full_name = get_formatted_name('Awad','Sharif','Zulfikhar')
        self.assertEqual(full_name, 'Awad Zulfikhar Sharif')
unittest.main()


