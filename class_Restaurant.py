class Restaurant():

    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.customers_served = 0
        

    def restaurant_info(self):
        return "The restaurant %s serves %s food." %(self.name,self.cuisine_type)

    def open_restaurant(self):
        return "Come in, %s is opened!" %(self.name)

    def number_served(self,customers):
        self.customers_served = customers
        return "The number of customers served at %s is %s." %(self.name,self.customers_served)
        
    def increment_number_served(self,increment):
        if increment >= 0:
            self.customers_served = self.customers_served + increment
            return "The number of customers served at %s is %s" %(self.name,self.customers_served)

##first_restaurant = Restaurant('Lotus','Chinese')
##first_restaurant.number_served(500)
##first_restaurant.increment_number_served(176)

class IceCreamStand(Restaurant):
#The * takes in infinite number of arguments!    
    def __init__(self,*flavors):
        self.flavors = flavors
        self.total = []


    def ice_cream_flavors(self):
        for flavor in self.flavors:
            self.total.append(flavor)
        print (self.total)

