import unittest

class Employee():

    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def add_Raise(self,salary_raise):
        bonus = 5000
##Add a 5000 custom raison if no salary_raise is provided
        if salary_raise == 0:
            total = int(self.salary) + bonus
##Else add the custom raise provided
        elif salary_raise > 0:
            total = int(self.salary) + int(salary_raise)
        return total

class TestEmployeeClass(unittest.TestCase):

    def setUp(self):
        self.first_employee = Employee('Awad','Sharif',65000)

    def test_add_Raise(self):
        self.first_employee.add_Raise(0)
        self.assertEqual(self.first_employee.add_Raise(0),70000)

    def test_custom_raise(self):
        total = self.first_employee.add_Raise(2000)
        self.assertEqual(total,67000)
unittest.main()

