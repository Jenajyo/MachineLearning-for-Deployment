class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    
    def check_balance(self):
        print(f'The remaining balance in the account is ${self.balance}')
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print(f'Deposit of ${dep_amt} Accepted,Current Balance is ${self.balance}')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'Withdrawal of ${wd_amt} Accepted,Current Balance is ${self.balance}')
            check_balance(self)
        else:
            print(f'Funds Unavailable!,Current Balance is ${self.balance}')
            
class MinimumBalanceAccount(Account):
    
    min_bal=5000
    
    def __init__(self,owner,balance):
        Account.__init__(self,owner,balance)
        if balance<5000:
            raise Exception("Minimum Account Balance to be mantained is 5000")
        
    
    def withdraw(self,wd_amt):
        if self.balance-self.min_bal >= wd_amt:
            self.balance -= wd_amt
            print(f'Withdrawal of ${wd_amt} Accepted,Current Balance is ${self.balance}')
        else:
            print(f'Funds Unavailable!,Current Balance is ${self.balance}')
            
    