class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def restock(self, amount):
        self.stock += amount

    def sell(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return self.price * quantity
        else:
            print(f"Not enough stock for {self.name}")
            return 0

class Register:
    def __init__(self):
        self.products = {}
        self.sales = 0
        self.transactions = []
        self.shifts = {}

    def add_product(self, name, price, stock):
        self.products[name] = Product(name, price, stock)

    def restock_product(self, name, quantity):
        if name in self.products:
            self.products[name].restock(quantity)
        else:
            print(f"Product {name} not found")

    def sell_product(self, name, quantity):
        if name in self.products:
            sale_amount = self.products[name].sell(quantity)
            self.sales += sale_amount
            self.transactions.append((name, quantity, sale_amount))
        else:
            print(f"Product {name} not found")

    def start_shift(self, shift_id):
        self.shifts[shift_id] = {
            'start_sales': self.sales,
            'end_sales': 0,
            'transactions': []
        }

    def end_shift(self, shift_id):
        if shift_id in self.shifts:
            self.shifts[shift_id]['end_sales'] = self.sales
            self.shifts[shift_id]['transactions'] = self.transactions

    def daily_financial_report(self):
        total_sales = sum(shift['end_sales'] - shift['start_sales'] for shift in self.shifts.values())
        print(f"Total Sales for the Day: ${total_sales:.2f}")

    def inventory_report(self):
        print("Inventory Report:")
        for product in self.products.values():
            print(f"{product.name}: {product.stock} units")

def main():
    register = Register()

    while True:
        print("\nChoose an action:")
        print("1. Add Product")
        print("2. Restock Product")
        print("3. Sell Product")
        print("4. Start Shift")
        print("5. End Shift")
        print("6. Daily Financial Report")
        print("7. Inventory Report")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter initial stock: "))
            register.add_product(name, price, stock)
            print(f"Added {name} to the register.")

        elif choice == "2":
            name = input("Enter product name: ")
            quantity = int(input(f"Enter quantity to restock for {name}: "))
            register.restock_product(name, quantity)

        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input(f"Enter quantity to sell for {name}: "))
            register.sell_product(name, quantity)

        elif choice == "4":
            shift_id = input("Enter shift ID: ")
            register.start_shift(shift_id)
            print(f"Shift {shift_id} started.")

        elif choice == "5":
            shift_id = input("Enter shift ID to end: ")
            register.end_shift(shift_id)
            print(f"Shift {shift_id} ended.")

        elif choice == "6":
            register.daily_financial_report()

        elif choice == "7":
            register.inventory_report()

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
