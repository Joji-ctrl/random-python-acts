class Product:
        def __init__(self):
            self.pname = pname
            self.pprice = price
            self.pquan = pquan

        def total_cost(self):
            total = self.pquan * self.pprice
            return total

class ElectronicProduct(Product):
    def __init__(self):
        self.pname = input("Product Name: ")
        self.pprice = int(input("Product Price: "))
        self.pquan = int(input("Product Quantity: "))
        self.warranty_period = input("Warranty Period: ")

    def dispinfo(self):
        print(f"Product: {self.pname}\nPrice per unit: {self.pprice}\nQuantity: {self.pquan}\nTotal Cost: {super().total_cost()}\nWarranty Period: {self.warranty_period}")

class GroceryProduct(Product):
    def __init__(self):
        self.pname = input("Product Name: ")
        self.pprice = int(input("Product Price: "))
        self.pquan = int(input("Product Quantity: "))
        self.expiry = input("Expiry Date: ")

    def dispinfo(self):
        print(f"Product: {self.pname}\nPrice per unit: {self.pprice}\nQuantity: {self.pquan}\nExpiry Date: {self.expiry}")


print("Available product operations:\n1 - Add an electric product\n2 - Add a grocery product\nType 'q' to quit\n")
x = input("1, 2, or q: ")

if x == '1':
    product1 = ElectronicProduct()
    product1.dispinfo()
elif x == '2':
    product1 = GroceryProduct()
    product1.dispinfo()
elif x == 'q':
    print("You chose to quit.")
else:
    print("Invalid Option, terminating program")
