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

class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        # print(self.__balance) 错误的
        return super().withdraw(amount + self.withdraw_fee)
        
        # return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
    """A bank has accounts
    
    >>> bank = Bank()
    >>> john = bank.open_account('Jhon', 10)
    >>> jack = bank.open_account('jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.get_balance()
    10.2
    """
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind = Account):
        ac = kind(holder)
        ac.deposit(amount)
        self.accounts.append(ac)
        return ac # ac 是一个 instance, 不是字面量, 因此修改 ac, self.account 里的 ac 的内容也会随之变化, 是同一个 ac

    def pay_interest(self):
        for ac in self.accounts:
            ac.deposit(ac.interest * ac.get_balance())
    
    def too_big_to_fail(self):
        return len(self.accounts) > 1