class User:
    def __init__(self, name, email, password, deposit):
        self.name = name
        self.email = email
        self.password = password
        self.balance = deposit
        self.trans_history = []

    def deposit(self, amount):
        self.balance += amount
        self.trans_history.append(f'The deposit is {amount} and account balance is {self.balance}.')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.trans_history.append(f'The withdrawal amount is {amount} and account balance is {self.balance}.')
        else:
            print('The bank is bankrupt')

    def get_loan(self, loan_amount):
        if self.balance * 2 >= loan_amount:
            self.balance += loan_amount
            self.trans_history.append(f'The loan amount is {loan_amount} and account balance is {self.balance}.')
        else:
            print('You are not eligible for a loan')

    def transfer_money(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
            self.trans_history.append(f'The transfer amount is {amount} and account balance is {self.balance}.')
        else:
            print('The bank is bankrupt')


class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan = 0
        self.loan_enabled = True

    def create_account(self, name, email, password, deposit):
        user = User(name, email, password, deposit)
        self.users.append(user)
        self.total_balance += deposit

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def deposit(self, user, amount):
        user.deposit(amount)
        self.total_balance += amount

    def withdraw(self, user, amount):
        if amount <= user.balance:
            user.withdraw(amount)
            self.total_balance -= amount
        else:
            print('The bank is bankrupt')

    def transfer(self, sender, receiver, amount):
        if amount <= sender.balance:
            sender.transfer_money(receiver, amount)
        else:
            print('The bank is bankrupt')

    def check_balance(self, user):
        return user.balance

    def get_transaction_history(self, user):
        return user.trans_history

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan(self):
        return self.total_loan

    def enable_loan(self):
        self.loan_enabled = True

    def disable_loan(self):
        self.loan_enabled = False

    def give_loan(self, user):
        if self.loan_enabled and self.total_balance >= user.balance * 2:
            loan_amount = user.balance
            user.get_loan(loan_amount)
            self.total_loan += loan_amount
        else:
            print('Loan is currently unavailable')


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, password, deposit):
        self.bank.create_account(name, email, password, deposit)

    def get_total_balance(self):
        return self.bank.get_total_balance()

    def get_total_loan(self):
        return self.bank.get_total_loan()

    def enable_loan(self):
        self.bank.enable_loan()

    def disable_loan(self):
        self.bank.disable_loan()



Alif = Bank()
admin = Admin(Alif)

admin.create_account('Abul Uddin', 'abul@uddin.com', '1234567', 8000)
admin.create_account('Kasem Ali', 'kasem@ali.com', '2874872', 11000)

abul = Alif.get_user('Abul Uddin')
kasem = Alif.get_user('Kasem Ali')

admin.enable_loan()

Alif.deposit(abul, 3000)
Alif.deposit(kasem, 1500)

Alif.withdraw(abul, 2000)
Alif.transfer(abul, kasem, 500)
Alif.withdraw(kasem, 16000)

Alif.give_loan(abul)
Alif.give_loan(kasem)

print(Alif.check_balance(abul))
print(Alif.check_balance(kasem))

print(Alif.get_transaction_history(abul))
print(Alif.get_transaction_history(kasem))

print(admin.get_total_balance())
print(admin.get_total_loan())
