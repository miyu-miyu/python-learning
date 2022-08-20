class Account:
    interest = 0.02
    # __balance = 1 # private membert
    def __init__(self, account_holder):
        self.__balance = 0
        # self.interest = 0.1
        self.holder = account_holder

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        self.ok = 'ok' # deposit invoked, the `ok` can be access
        return self.__balance
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insuficient funds"
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    

a = Account("Miyu")
