# 4. Class Variables and Class Methods
# Assignment:Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing
# the bank name. Show that it affects all instances.

class Bank:
    old_bank_name = "Central Bank"

    @classmethod
    def change_bank_name(cls, new_bank_name):
        cls.old_bank_name = new_bank_name

bank = Bank()
print(Bank.old_bank_name)
bank.change_bank_name("commercial_bank")
print(bank.old_bank_name)
