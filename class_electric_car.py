class Car():
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
#set attribute to default number so that we can change it in the methods!!
        self.odometer_reading = 0
        
    def car_info(self):
        print "It's a %s %s %s" %(self.year,self.make,self.model)

    def odometer(self):
        print "The odometer reading is %s" %(self.odometer_reading)

    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        print self.odometer_reading

    def increment_odometer(self,miles):
        if miles >= 0:
            self.odometer_reading = self.odometer_reading + miles
            print self.odometer_reading



##Create a Battery class to add all your battery info instead of ElectricCar.

class Battery():
    def __init__(self):
        self.battery_size = 75

    def battery_info(self):
        print "The battery size is %s" %(self.battery_size)

    def upgrade_battery(self,size):
        if size > 0:
            self.battery_size = self.battery_size + size
        print "The new battery size is " + str(self.battery_size) + "." + "\n" 
        if (self.battery_size > 85):
            print "The battery size is bigger than 85!"

class ElectricCar(Car):

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

#create an instance of 'Battery' class under the ElectricCar class
#instance name is self.batteries!
        self.batteries = Battery()

tesla = ElectricCar("Tesla","S","2015")
#first call instance, then attribute assigned and the method in it!!
tesla.batteries.battery_info()
tesla.batteries.upgrade_battery(15)
    
