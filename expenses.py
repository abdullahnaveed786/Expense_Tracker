import csv
from datetime import datetime

class Expense_Tracker:
    def __init__(self, filename):
        self.filename = filename
        self.expenses = self.load_expenses()

    # -------------------- File Operations --------------------
    def load_expenses(self):
        expenses = []
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    expense = {
                        "name": row["name"],
                        "amount": float(row["amount"]),
                        "category": row["category"],
                        "date": row["date"]
                    }
                    expenses.append(expense)
        except FileNotFoundError:
            pass  # If file doesn't exist, start with empty list
        return expenses

    def save_expenses(self):
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["name", "amount", "category", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    # -------------------- Expense Operations --------------------
    def add_expense(self, name, amount, category):
        date = datetime.now().strftime("%Y-%m-%d")
        expense = {
            "name": name.lower(),
            "amount": amount,
            "category": category.lower(),
            "date": date
        }
        self.expenses.append(expense)

    def delete_expense(self, name):
        for expense in self.expenses:
            if expense["name"].lower() == name.lower():
                self.expenses.remove(expense)
                return True
        return False

    # -------------------- Display / Summary --------------------
    def display_all(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\n----------------------------------------------------------")
        print(f"{'Name':<15}{'Amount':<10}{'Category':<15}{'Date'}")
        print("----------------------------------------------------------")

        for expense in self.expenses:
            print(
                f"{expense['name']:<15}"
                f"{expense['amount']:<10.2f}"
                f"{expense['category']:<15}"
                f"{expense['date']}"
            )

    def get_category_total(self, category):
        return sum(
            expense["amount"]
            for expense in self.expenses
            if expense["category"].lower() == category.lower()
        )

    def get_monthly_summary(self):
        summary = {}
        for expense in self.expenses:
            month = expense["date"]
            if month not in summary:
                summary[month] = 0
            summary[month] += expense["amount"]
        return summary

    def filter_by_month(self, month):
        return [
            expense for expense in self.expenses
            if expense["date"] == month
        ]

    def get_most_expensive(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda e: e["amount"])