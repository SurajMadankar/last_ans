class Account:
    balance=0
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
        
    def title(self):
        print(self.title)
    def balance(self):
        return(self.balance)
    def deposit(self,amount):
        balance=self.balance+amount
        return balance
    def getbalance(self,amount):
        balance=self.balance+amount
        print(balance)
    def withdrawal(self,amount):
        balance=self.balance-amount
        print(balance)
          
         
class SavingsAccount(Account):

    def __init__(self,title,balance,interstRate):
        super().__init__(title, balance)
        self.interestRate=interstRate
    def  interestamount(self):
        interestamount=self.interestRate*self.balance
        c=interestamount/100
        print(c)


a=Account("Ashish",2000)
(a.getbalance(500))
# print(a.deposit(500))
a.withdrawal(500)

b=SavingsAccount("Ashish",2000,5)
b.interestamount()