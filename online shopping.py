# Defining the Product class
class Product:
    # Constructor to initialize product details
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    # Method to display product information
    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Stock: {self.quantity_in_stock}")

# Defining the ShoppingCart class
class ShoppingCart:
    # Class variable to track the total number of carts created
    total_carts = 0

    # Constructor to initialize cart details
    def __init__(self):
        self.items = []  # List to store products and their quantities
        ShoppingCart.total_carts += 1  # Increment total carts count when a new cart is created

    # Method to add a product to the cart if quantity is available
    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Decrease the stock of the product
        else:
            print(f"Not enough stock for {product.product_name}! Only {product.quantity_in_stock} available.")

    # Method to remove a product from the cart
    def remove_from_cart(self, product):
        self.items = [(item, qty) for item, qty in self.items if item != product]

    # Method to display all items in the cart
    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for product, quantity in self.items:
                print(f"{product.product_name}: {quantity} @ {product.price} each")

    # Method to calculate the total price of items in the cart
    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items)
        return total


# Creating Product objects with varying prices and quantities
product_1 = Product("Laptop", 1200, 10)
product_2 = Product("Smartphone", 800, 20)
product_3 = Product("Headphones", 150, 30)

# Creating two separate ShoppingCart instances
cart_1 = ShoppingCart()
cart_2 = ShoppingCart()

# Performing operations on cart_1
cart_1.add_to_cart(product_1, 1)  # Adding 1 Laptop to Cart 1
cart_1.add_to_cart(product_3, 2)  # Adding 2 Headphones to Cart 1
cart_1.display_cart()  # Displaying contents of Cart 1
print(f"Total for Cart 1: ${cart_1.calculate_total():.2f}\n")  # Displaying total for Cart 1

# Performing operations on cart_2
cart_2.add_to_cart(product_2, 1)  # Adding 1 Smartphone to Cart 2
cart_2.add_to_cart(product_3, 1)  # Adding 1 Headphones to Cart 2
cart_2.remove_from_cart(product_3)  # Removing Headphones from Cart 2
cart_2.display_cart()  # Displaying contents of Cart 2
print(f"Total for Cart 2: ${cart_2.calculate_total():.2f}\n")  # Displaying total for Cart 2

# Displaying product information for all products after transactions
print("Product Stock after transactions:")
product_1.display_product_info()
product_2.display_product_info()
product_3.display_product_info()
