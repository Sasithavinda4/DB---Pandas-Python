# Product class

class Product:
    def __init__(self,product_id,name,quantity,price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_total_value(self):
        return self.quantity * self.price

    def display_product_details(self):
        print("ID: ",self.product_id, "Name: ",self.name, "Quantity: ",self.quantity, "Price: ",self.price)


# InventorySystem class

class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        if product.product_id in self.inventory.keys():
            print("Product already exists")
            return None
        self.inventory[product.product_id] = product
        print("Product added successfully....")

    def update_product_quantity(self, product_id, new_quantity):
        if product_id in self.inventory.keys():
            self.inventory[product_id].update_quantity(new_quantity)
            print("Product quantity updated successfully....")
        else:
            print("No product found for the given ID")

    def remove_product(self, product_id):
        if product_id in self.inventory.keys():
            self.inventory[product_id] = None
            print("Product removed successfully....")
        else:
            print("No product found for the given ID")

    def view_inventory(self):
        if len(self.inventory) == 0:
            print("Inventory is empty")
        else:
            print("Inventory Details:")
            for items in self.inventory.values():
                if items is not None:
                    items.display_product_details()

# File operations
    
    def generate_sales_report(self, filename):
        file = open(filename, "w")
        file.write("Product ID, Name, Quantity, Total Value\n")
        for p in self.inventory.values():
            if p is not None:
                details = (
                    p.product_id
                    + ", "
                    + p.name
                    + ", "
                    + str(p.quantity)
                    + ", $"
                    + str(p.get_total_value())
                    + "\n"
                )
                file.write(details)
        file.close()
        print("Sales report saved successfully....")

    def load_inventory_from_file(self, filename):
        try:
            file = open(filename, "r")
            lines = file.readlines()[1:]
            for line in lines:
                product_id, name, quantity, price = line.strip().split(", ")
                product = Product(
                    product_id, name, int(quantity), float(price.replace("$", ""))
                )
                self.add_product(product)
            file.close()
            print("Inventory loaded successfully....")
        except FileNotFoundError:
            print("File not found!")


# Implement a menu-driven system

def main():
    inventory_system = InventorySystem()
    print("....Welcome to the Grocery Inventory System....")

    while True:
        print("\n1.Add Products to Inventory")
        print("2.Update Product Quantity")
        print("3.Remove Products from Inventory")
        print("4.View Inventory Details")
        print("5.Generate Sales Report")
        print("6.Load Inventory from File")
        print("7.Exit\n")

        option = int(input("Enter Your Option: "))

        if option == 1:
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price per Unit: "))
            product = Product(product_id,name,quantity,price)
            inventory_system.add_product(product)

        elif option == 2:
            product_id = input("Enter Product ID: ")
            new_quantity = int(input("Enter New Quantity: "))
            inventory_system.update_product_quantity(product_id,new_quantity)

        elif option == 3:
            product_id = input("Enter Product ID: ")
            inventory_system.remove_product(product_id)

        elif option == 4:
            inventory_system.view_inventory()

        elif option == 5:
            filename = input("Enter File Name to Save Report: ")
            inventory_system.generate_sales_report(filename)

        elif option == 6:
            filename = input("Enter File Name to Load Inventory: ")
            inventory_system.load_inventory_from_file(filename)

        elif option == 7:
            print("Exiting.... Goodbye!")
            break

        else:
            print("Invalid Option! Please Try Again....")


main()
