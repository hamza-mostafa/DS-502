from decimal import Decimal


class BankAccount:
    def __init__(self, initial_balance: Decimal=0.00):
        self.balance = Decimal(initial_balance)

    def transaction(self, t_type: str, amount: Decimal):
        if amount > 0:
            if t_type == "deposit":
                self.balance += Decimal(amount)
            elif t_type == "withdraw":
                if amount > self.balance:
                    raise ValueError("Insufficient funds")
                self.balance -= Decimal(amount)
            else:
               raise Exception(f"Unknown transaction type: {t_type}")
            print(f"{t_type}: EGP {amount:.2f}, new balance: {self.balance:.2f}")
        else:
            raise Exception("Amount must be positive.")

    def deposit(self, amount: Decimal):
        return self.transaction("deposit", amount)

    def withdraw(self, amount: Decimal):
        return self.transaction("withdraw", amount)

    def check_balance(self):
        return self.balance
