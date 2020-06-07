
class Product():
    def __init__(self,name,price,category,id):
        self.name = name
        self.price = price
        self.category = category
        self.product_id = id

    def update_price(self,percent_change,is_increased):
        percent_change /= 100
        if is_increased:
            self.price += (self.price*percent_change)

        else:
            self.price -= (self.price*percent_change)
        return self

    def print_info(self):
        print("Name of product: " , self.name)
        print("Category: ", self.category)
        print("Price of product $", self.price)
        print("Product id = " , self.product_id)
        print("\n")

class Store():
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self,name,price,category,id):
        self.products.append(Product(name,price,category,id))
        return self

#Remove a product by its id

    def sell_product(self,id):
        for product in self.products:
            if product.product_id == id:
                self.products.remove(product)
                print("Removing following product: \n")
                product.print_info()
        return self

#increase prices for ALL products

    def inflation(self,percent_change,is_increased=True):
        for product in self.products:
            product.update_price(percent_change,is_increased=True)
            print("Price after inflation for all products: \n")
            product.print_info()
        return self

#set discount for items under specific category only!

    def set_clearance(self,category,percent_change):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_change,is_increased=False)
                print("Price after discount for " + category + ": \n")
                product.print_info()
        return self 
        

store = Store('Target')
store.add_product('Shirt',13.50,'Clothes',1234).add_product('Pants',9.75,'Clothes',3021).add_product('Coke',1.25,'Soda',7683).sell_product(7683).inflation(12)
        





        

    

    


            

    
