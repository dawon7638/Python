class BankAccount:
    def __init__(self, name, balance, int_rate):
        self.name = name
        self.int_rate = int_rate
        self.account_balance = balance
        
     # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
        
    # adding the withdraw method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
        
    # adding the yield method
    def yied_interest(self):
        self.account_balance += self.account_balance * self.int_rate  
        return self
        
    # adding the display account method
    def display_account_info(self):
        print(f"Name: {self.name}, Interest Earned: {self.int_rate}, Balance: {self.account_balance}")
        return self
        
        
        
acctOne = BankAccount("acctOne", 0, 0.02)
acctTwo = BankAccount("acctTwo", 0, 0.05)

acctOne.make_deposit(1000).make_deposit(1000).make_withdrawal(450).yied_interest().display_account_info()

acctTwo.make_deposit(1000).make_deposit(1000).make_withdrawal(100).make_withdrawal(50).make_withdrawal(150).make_withdrawal(250).yied_interest().display_account_info()
