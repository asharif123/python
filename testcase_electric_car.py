##test Car class
from class_electric_car import Car, Battery
import unittest

class TestCarClass(unittest.TestCase):

    def setUp(self):
        self.my_car = Car('Buick','Verrano',2014)
        self.odometer_reading = 0
        return self.odometer_reading
unittest.main()
