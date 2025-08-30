form typing import List
class BankAccount:
    def __init__(self,name,balance):
        self.__name = name
        self.__balance = balance

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
    def getBalance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

if __name__ == "__main__":
    amount = BankAccount("Tanush",1000)

    print("Account Holder Name : ",amount.getName())
    print("Account Holder Name : ",amount.getBalance())

    amount.deposit(1500)
    print(amount.getBalance())
        
        
    