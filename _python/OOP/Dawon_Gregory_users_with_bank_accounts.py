class User:
    def __init__(self, name, balance, int_rate):
        self.name = name
        self.account = balance
        self.int_rate = int_rate
        
    # adding the deposit method
    def make_deposit(self, amount):
        self.account += amount
        return self
    
    # adding user account method
    def display_user_balance(self):
        print(f"Name: {self.name}, Interest Earned: {self.int_rate}, Balance: {self.account}")
        return self
    
    # adding the withdrawl method
    def make_withdrawal(self, amount):
        self.account -= amount
        return self
    
    # adding the yield method
    def yield_interest(self):
        self.account += self.account * self.int_rate  
        return self
        
        
               
dawon = User("Dawon Gregory", 0.02, 0)

gregerson = User("Gregerson Lowe", 0.05, 0)

tommy = User("Thomas Jefferson", 0.09, 0)

        

dawon.make_deposit(1000).make_deposit(1000).make_withdrawal(450).yield_interest().display_user_balance()
             
gregerson.make_deposit(1000).make_deposit(1000).make_withdrawal(100).make_withdrawal(50).make_withdrawal(150).make_withdrawal(250).yield_interest().display_user_balance()

tommy.make_deposit(5000).make_withdrawal(250).make_withdrawal(250).make_withdrawal(250).yield_interest().display_user_balance()

