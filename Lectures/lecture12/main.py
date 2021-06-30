class Payment:
    def __init__(self, amount):
        self.amount = amount
    
    def make_payment(self):
        print("Payment is initiated !")
        self.pay()

    def pay(self):
        print(" Payment is made by default")


class Cod (Payment):
        def __init__(self, amount):
            self.amount = amount
            super().__init__(amount)
        
        def pay(self):
            print("Payment is made by COD.")

class Card (Payment):
        def __init__(self, amount):
            self.amount = amount
            super().__init__(amount)
        
        def pay(self):
            print("Payment is made by card.")

cod = Cod(1000)
cod.make_payment()


        

