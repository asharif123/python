import unittest

##test out city_function
from city_functions import city_info

class testLocationInfo(unittest.TestCase):

    def test_city_country(self):
        location_name = city_info('Santiago','Chile')
        #print location_name
        self.assertEqual(location_name, 'Santiago Chile')

    def test_city_country_population(self):
        full_info = city_info('Santiago','Chile','500000')
        self.assertEqual(full_info, 'Santiago Chile - population = 500000')
unittest.main()


