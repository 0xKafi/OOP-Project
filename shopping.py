
class User:
    cs_data = {}
    sl_data = {}
    product_list = {}
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
    
    @staticmethod
    def check_info(username, password, id):
        if(id == 1):
            if username not in User.cs_data:
                return -1
            elif(User.cs_data[username] == password):
                return 1
        elif(id == 2):
            if username not in User.sl_data:
                return -1
            elif(User.sl_data[username] == password):
                return 1
        return 0


class Customer(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        User.cs_data[username] = self.password

class Seller(User):
    def __init__(self, username, password) -> None:
        super().__init__(username, password)
        User.sl_data[username] = self.password

class Product:
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

class Store():
    products = {}

    def add_product(self, username, name, price, quantity):
        if username not in self.products:
            self.products[username] = {}
        self.products[username][name] = (Product(name, price, quantity))

    def view_product(self):
        print("\n")
        for key in self.products.keys():
            for sec_key in self.products[key].keys():
                print(self.products[key][sec_key].name, self.products[key][sec_key].price, self.products[key][sec_key].quantity)
                
            
class Order(Store):
    def __init__(self) -> None:
        super().__init__()
        self.checkout = []

    def buy_an_item(self, item, num):
        for key in self.products.keys():
            if item not in self.products[key].keys():
                print(f"Item Not Found!")
            elif (self.products[key][item].quantity < num):
                print(f"You Can Buy UpTo {self.products[key][item].quantity} quantity of this {item}")
            else:
                cost = self.products[key][item].price * num
                self.checkout.append((item,cost))
                print(f"cost of this {item}: {cost}tk")

while True:
    print("\n--> Main Page:\n  Press 1 for Sign Up As a Customer\n  Press 2 for Sign Up As a Seller\n  Press 3 for Login\n  --> ",end = "")
    btn1 = int(input())
    if(btn1 == 1):
        print("  Enter Your Username: ",end = "")
        nam = input()
        print("  Enter Your Password: ",end = "")
        pas = input()
        cs = Customer(nam, pas)
        print(f"Customer {nam} registered successfully!")


    elif(btn1 == 2):
        print("  Enter Your Username: ",end = "")
        nam = input()
        print("  Enter Your Password: ",end = "")
        pas = input()
        sl = Seller(nam, pas)
        print(f"Seller {nam} registered successfully!")



    elif(btn1 == 3):
        print("  Press 1 for Customer\n  Press 2 for Seller\n  --> ",end = "")
        btn2 = int(input())
        if(btn2 == 1):
            print("  Enter Your Username: ",end = "")
            nam = input()
            print("  Enter Your Password: ",end = "")
            pas = input()
            bol = User.check_info(nam, pas, 1)

            if(bol == 0):
                print("Verification Failed! Please try again.")
                continue
            elif(bol == -1):
                print(f"--> You don't have account!")
                continue
            print(f"\n--> Login successful. Welcome, {nam}! <--\n")


        elif(btn2 == 2):
            print("  Enter Your Username: ",end = "")
            nam = input()
            print("  Enter Your Password: ",end = "")
            pas = input()
            bol = User.check_info(nam,pas, 2)
            if(bol == 0):
                print("Verification Failed! Please try again.")
                continue
            elif(bol == -1):
                print(f"--> You don't have account!")
                continue
            print(f"\n--> Login successful. Welcome, {nam}! <--\n")

            while True:
                print("  Press 1 for Add Product\n  Press 2 for back to Main Page\n  --> ",end = "")
                btn3 = int(input())
                if(btn3 == 1):
                    print("  Enter Product Name: ",end = "")
                    pro_nam = input()
                    print("  Enter Product Price: ",end = "")
                    pro_price = int(input())
                    print("  Enter Product Quantity: ",end = "")
                    pro_quant = int(input())

                    store = Store()
                    store.add_product(nam, pro_nam, pro_price, pro_quant)
                    print(f"Product Name: {pro_nam}, Price: {pro_price}, Quantity: {pro_quant} added succesfully.")
                    
                elif(btn3 == 2):
                    break
                else:
                    print("Invalid Choice.")

        else:
             print("Invalid Choice.")

    else:
         print("Invalid Choice.")
