import csv
import os
file_name = "expenses.csv"
def init_csv():
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
def add_expense(date, category, amount, description):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")
def view_expenses():
    if not os.path.exists(file_name):
        print("No expenses recorded yet.")
        return

    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
def total_expenses():
    if not os.path.exists(file_name):
        print("No expenses recorded yet.")
        return

    total = 0.0
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            total += float(row[2])
    print(f"Total expenses: {total}")
def main():
    init_csv()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(date, category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
