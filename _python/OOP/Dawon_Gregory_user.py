class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.account_balance = balance

       
    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        
    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: {self.account_balance}")
        
    # adding the withdrawl method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
        
               
dawon = User("Dawon Gregory", "account_balance@gmails.com", (20))
gregerson = User("Gregerson Lowe", "fomo@google.net", (20))
tommy = User("Thomas Jefferson", "foundingfathers@aol.com", (20))
        

dawon.make_deposit(1000)               
dawon.make_deposit(1000)               
dawon.make_deposit(1000)
dawon.display_user_balance()


gregerson.make_deposit(1000)
gregerson.make_deposit(1000)              
gregerson.make_withdrawal(100)
gregerson.make_withdrawal(50)
gregerson.display_user_balance()

tommy.make_deposit(5000)
tommy.make_withdrawal(250)
tommy.make_withdrawal(250)
tommy.make_withdrawal(250)
tommy.display_user_balance()




