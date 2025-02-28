# Expense Tracker in Python
expenses = []

def add_expense(amount, category):
    expenses.append({"amount": amount, "category": category})
    print("Expense added successfully!")

def show_expenses():
    for expense in expenses:
        print(f"₹{expense['amount']} - {expense['category']}")

# Example Usage
add_expense(500, "Food")
add_expense(1000, "Transport")
show_expenses()
