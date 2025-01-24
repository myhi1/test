class RedBlackTree:
    def __init__(self):
        # Initialize an empty list to simulate a sorted red-black tree.
        self.values = []

    def insert(self, value):
        # Insert a value into the sorted list in the correct position.
        # This ensures the list remains sorted at all times.
        if not self.values:
            self.values.append(value)
        else:
            i = 0
            while i < len(self.values) and self.values[i] < value:
                i += 1
            self.values.insert(i, value)

    def remove(self, value):
        # Remove a value from the list if it exists.
        if value in self.values:
            self.values.remove(value)

    def find_median(self):
        # Calculate the median of the values in the list.
        n = len(self.values)
        if n == 0:
            return None  # Return None if the list is empty.
        if n % 2 == 1:
            return self.values[n // 2]  # Median for odd-length list.
        else:
            return (self.values[n // 2 - 1] + self.values[n // 2]) / 2  # Median for even-length list.

    def range_query(self, low, high):
        # Retrieve all values within the specified range [low, high].
        return [v for v in self.values if low <= v <= high]

class Store:
    def __init__(self):
        # Initialize the store with an empty product catalog and a red-black tree for prices.
        self.products = {}  # Dictionary to store product details by barcode.
        self.price_tree = RedBlackTree()  # Red-black tree for price management.

        # Pre-populate the store with initial products.
        self.add_product("kafsh", "1", 890000)
        self.add_product("kif", "2", 1500000)
        self.add_product("loptop", "3", 47000000)

    def add_product(self, name, barcode, price):
        # Add a new product to the store.
        # If the barcode already exists, notify the user and do not add.
        if barcode in self.products:
            print(f"Product with barcode {barcode} already exists.")
            return

        self.products[barcode] = {
            "name": name,
            "prices": [price],  # Maintain a history of prices.
            "current_price": price  # Store the current price.
        }

        self.price_tree.insert(price)  # Add the price to the red-black tree.
        print(f"Product {name} added successfully.")

    def remove_product(self, barcode):
        # Remove a product from the store based on its barcode.
        if barcode not in self.products:
            print(f"Product with barcode {barcode} not found.")
            return

        product = self.products.pop(barcode)  # Remove product from the catalog.
        self.price_tree.remove(product["current_price"])  # Remove its price from the tree.
        print(f"Product {product['name']} removed successfully.")

    def update_price(self, barcode, new_price):
        # Update the price of a product based on its barcode.
        if barcode not in self.products:
            print(f"Product with barcode {barcode} not found.")
            return

        product = self.products[barcode]
        old_price = product["current_price"]
        self.price_tree.remove(old_price)  # Remove the old price from the tree.

        product["prices"].append(new_price)  # Add the new price to the price history.
        product["current_price"] = new_price  # Update the current price.

        self.price_tree.insert(new_price)  # Insert the new price into the tree.

        median = self.price_tree.find_median()  # Calculate the new median.
        if median is not None:
            print(f"Price updated. New median price: {median}")

    def calculate_median(self):
        # Calculate the median price of all products in the store.
        return self.price_tree.find_median()

    def list_products_in_range(self, min_price, max_price):
        # List all products with prices within a specified range.
        result = []
        for barcode, product in self.products.items():
            if min_price <= product["current_price"] <= max_price:
                result.append((barcode, product["name"]))
        return result

    def list_cheaper_and_costlier(self, barcode):
        # List products that are cheaper or costlier than a given product.
        if barcode not in self.products:
            print(f"Product with barcode {barcode} not found.")
            return

        current_price = self.products[barcode]["current_price"]
        cheaper = [b for b, p in self.products.items() if p["current_price"] < current_price]
        costlier = [b for b, p in self.products.items() if p["current_price"] > current_price]

        print(f"Cheaper products: {cheaper}")
        print(f"Costlier products: {costlier}")

    def show_all_products(self):
        # Display all products in the store along with their details.
        if not self.products:
            print("No products in the store.")
            return

        print("\nList of all products:")
        for barcode, product in self.products.items():
            print(f"Barcode: {barcode}, Name: {product['name']}, Current Price: {product['current_price']}")

# User interface for managing the store.
if __name__ == "__main__":
    store = Store()

    while True:
        # Display menu options for the user.

        print("\n░▒█▀▀▀█░▀█▀░▄▀▀▄░█▀▀▄░█▀▀░░░▒█▀▄▀█░█▀▀▄░█▀▀▄░█▀▀▄░█▀▀▀░█▀▀░█▀▄▀█░█▀▀░█▀▀▄░▀█▀")
        print("░░▀▀▀▄▄░░█░░█░░█░█▄▄▀░█▀▀░░░▒█▒█▒█░█▄▄█░█░▒█░█▄▄█░█░▀▄░█▀▀░█░▀░█░█▀▀░█░▒█░░█░")
        print("░▒█▄▄▄█░░▀░░░▀▀░░▀░▀▀░▀▀▀░░░▒█░░▒█░▀░░▀░▀░░▀░▀░░▀░▀▀▀▀░▀▀▀░▀░░▒▀░▀▀▀░▀░░▀░░▀░")
        print("                         █▓▒░░amin & reza 2025░░▒▓█                          ")
        print("1. Add product")
        print("2. Remove product")
        print("3. Update product price")
        print("4. Show all products")
        print("5. List products in price range")
        print("6. List cheaper and costlier products")
        print("7. Calculate median price")
        print("8. Exit")

        choice = input("Enter your choice: ")
        print()  # Add a blank line for better readability.

        if choice == "1":
            # Add a new product by gathering necessary details from the user.
            name = input("Enter product name: ")
            barcode = input("Enter product barcode: ")
            price = float(input("Enter product price: "))
            store.add_product(name, barcode, price)

        elif choice == "2":
            # Remove a product by its barcode.
            barcode = input("Enter product barcode to remove: ")
            store.remove_product(barcode)

        elif choice == "3":
            # Update the price of an existing product.
            barcode = input("Enter product barcode to update price: ")
            new_price = float(input("Enter new price: "))
            store.update_price(barcode, new_price)

        elif choice == "4":
            # Display all products in the store.
            store.show_all_products()

        elif choice == "5":
            # List products within a specific price range.
            min_price = float(input("Enter minimum price: "))
            max_price = float(input("Enter maximum price: "))
            products = store.list_products_in_range(min_price, max_price)
            print("\nProducts in price range:")
            for barcode, name in products:
                print(f"Barcode: {barcode}, Name: {name}")

        elif choice == "6":
            # List products cheaper and costlier than a specified product.
            barcode = input("Enter product barcode: ")
            store.list_cheaper_and_costlier(barcode)

        elif choice == "7":
            # Calculate and display the median price of all products.
            median = store.calculate_median()
            if median is not None:
                print(f"Median price of all products: {median}")
            else:
                print("No products available to calculate median.")

        elif choice == "8":
            # Exit the program.
            print("Exiting the program. Goodbye!")
            break

        else:
            # Handle invalid menu choices.
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to return to the menu...")  # Wait for user to acknowledge before clearing output.
