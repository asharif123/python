#prints out the city, country and population (if population argument is provided!)u
import unittest
def city_info(city,country,population=''):
    if population:
        information = city.title() + ' ' + country.title() + " - population = " + population
    else:
        information = city.title() + ' ' + country.title()
    return information

class TestLocation(unittest.TestCase):

    def setUp(self):
        self.location = city_info('Tokyo','Japan','150000')

    def test_city(self):
        sentence = 'Tokyo Japan - population = 150000'
        self.assertEqual(sentence,self.location)
unittest.main()
