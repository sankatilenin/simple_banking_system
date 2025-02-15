import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Banking System")
        
        self.accounts = {}

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Account Creation
        tk.Label(self.root, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Initial Deposit:").grid(row=1, column=0)
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.grid(row=1, column=1)

        self.create_account_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.create_account_button.grid(row=2, columnspan=2)

        # Deposit
        tk.Label(self.root, text="Deposit Amount:").grid(row=3, column=0)
        self.deposit_amount_entry = tk.Entry(self.root)
        self.deposit_amount_entry.grid(row=3, column=1)

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=4, columnspan=2)

        # Withdraw
        tk.Label(self.root, text="Withdraw Amount:").grid(row=5, column=0)
        self.withdraw_amount_entry = tk.Entry(self.root)
        self.withdraw_amount_entry.grid(row=5, column=1)

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=6, columnspan=2)

        # Check Balance
        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance)
        self.check_balance_button.grid(row=7, columnspan=2)

    def create_account(self):
        name = self.name_entry.get()
        try:
            initial_deposit = float(self.deposit_entry.get())
            if initial_deposit < 0:
                raise ValueError("Initial deposit must be non-negative.")
            if name in self.accounts:
                messagebox.showerror("Error", "Account already exists.")
            else:
                self.accounts[name] = BankAccount(name, initial_deposit)
                messagebox.showinfo("Success", f"Account created for {name} with balance {initial_deposit}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def deposit(self):
        name = self.name_entry.get()
        try:
            amount = float(self.deposit_amount_entry.get())
            if name in self.accounts and self.accounts[name].deposit(amount):
                messagebox.showinfo("Success", f"Deposited {amount} to {name}'s account.")
            else:
                messagebox.showerror("Error", "Deposit failed. Check account name or amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid deposit amount.")

    def withdraw(self):
        name = self.name_entry.get()
        try:
            amount = float(self.withdraw_amount_entry.get())
            if name in self.accounts and self.accounts[name].withdraw(amount):
                messagebox.showinfo("Success", f"Withdrew {amount} from {name}'s account.")
            else:
                messagebox.showerror("Error", "Withdrawal failed. Check account name or amount.")
        except ValueError:
            messagebox.showerror("Error", "Invalid withdrawal amount.")

    def check_balance(self):
        name = self.name_entry.get()
        if name in self.accounts:
            balance = self.accounts[name].get_balance()
            messagebox.showinfo("Balance", f"{name}'s balance is {balance}.")
        else:
            messagebox.showerror("Error", "Account not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()