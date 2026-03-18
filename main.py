from expenses import Expense_Tracker  # Assuming your class is saved in expense_tracker.py


def print_menu():
    print("\n" + "="*50)
    print(f"{'Personal Expense Tracker':^50}")  
    print("="*50)
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total by category")
    print("4. View monthly summary")
    print("5. Exit")
    print("6. Delete expense")
    print("7. Filter expenses by month")
    print("8. Show most expensive expense")


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty.")
        else:
            return value


def main():
    filename = "data.csv"
    tracker = Expense_Tracker(filename)  # Create instance

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = get_non_empty_input("Enter name: ")
            category = get_non_empty_input("Enter category: ")
            amount = get_valid_amount()
            tracker.add_expense(name, amount, category)
            tracker.save_expenses()
            print("✅ Expense added successfully.")

        elif choice == "2":
            tracker.display_all()

        elif choice == "3":
            category = get_non_empty_input("Enter category: ")
            total = tracker.get_category_total(category)
            print(f"Total for {category}: £{total:.2f}")

        elif choice == "4":
            summary = tracker.get_monthly_summary()
            if not summary:
                print("No expenses recorded.")
            else:
                print("\nMonthly Summary:")
                for month, total in summary.items():
                    print(f"{month}: £{total:.2f}")

        elif choice == "5":
            print("Goodbye!")
            break

        elif choice == "6":
            name = get_non_empty_input("Enter expense name to delete: ")
            deleted = tracker.delete_expense(name)
            if deleted:
                tracker.save_expenses()
                print("Expense deleted.")
            else:
                print("Expense not found.")

        elif choice == "7":
            month = get_non_empty_input("Enter month (YYYY-MM-DD): ")
            filtered = tracker.filter_by_month(month)
            if not filtered:
                print("No expenses found for that month.")
            else:
                # Display filtered expenses without modifying tracker.expenses
                print("\nFiltered Expenses:")
                print("\n----------------------------------------------------------")
                print(f"{'Name':<15}{'Amount':<10}{'Category':<15}{'Date'}")
                print("----------------------------------------------------------")
                for expense in filtered:
                    print(
                        f"{expense['name']:<15}"
                        f"{expense['amount']:<10.2f}"
                        f"{expense['category']:<15}"
                        f"{expense['date']}"
                    )

        elif choice == "8":
            expense = tracker.get_most_expensive()
            if not expense:
                print("No expenses recorded.")
            else:
                print("\nMost Expensive Expense:")
                print(f"Name: {expense['name']}")
                print(f"Amount: £{expense['amount']:.2f}")
                print(f"Category: {expense['category']}")
                print(f"Date: {expense['date']}")

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()