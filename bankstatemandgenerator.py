class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class Acc:
    def __init__(self, customers, number, balance = 0):
        self.customers = customers
        self.number = number
        self.balance = 0
        self.op = []
        self.deposit(balance)
    #def info(self):
     #   print('Account N°: %s -- Balance %10.2f' %(self.number, self.balance))
    def withdraw(self, qty):
        if self.balance>=qty:
            self.balance -= qty
            self.op.append(['Withdraw:',qty])
    def deposit(self, qty):
        self.balance += qty
        self.op.append(['Deposit: ', qty])
    def statement(self):
        print('Extract CC N° %s' %self.number)
        for ope in self.op:
            print('%10s %10.2f' %(ope[0], ope[1]))
        print('%10s %10.2f' %('Balance = ', self.balance))
