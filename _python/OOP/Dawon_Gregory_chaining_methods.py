class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.account_balance = balance

       
    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    # adding user balance method
    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: {self.account_balance}")
        return self
    
    # adding the withdrawl method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
        
        
               
dawon = User("Dawon Gregory", "account_balance@gmails.com", (20))
gregerson = User("Gregerson Lowe", "fomo@google.net", (20))
tommy = User("Thomas Jefferson", "foundingfathers@aol.com", (20))

        

dawon.make_deposit(1000).make_deposit(1000).make_deposit(1000).display_user_balance()
             
gregerson.make_deposit(1000).make_deposit(1000).make_withdrawal(100).make_withdrawal(50).display_user_balance()

tommy.make_deposit(5000).make_withdrawal(250).make_withdrawal(250).make_withdrawal(250).display_user_balance()

