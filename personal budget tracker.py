# Define a transaction class to store income/expense details
class Transaction:
    def __init__(self, category, amount, is_expense):
        self.category = category
        self.amount = amount
        self.is_expense = is_expense

# Function to get user input for a transaction
def get_transaction_info():
    category = input("Enter category (e.g., Rent, Groceries): ")
    amount = float(input("Enter amount: "))
    is_expense = input("Is this an expense (y/n)? ").lower() == "y"
    return Transaction(category, amount, is_expense)

# Function to read transactions from a file (replace with database interaction for persistence)
def load_transactions():
    transactions = []
    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                category, amount, is_expense = line.strip().split(",")
                transactions.append(Transaction(category, float(amount), is_expense.lower() == "true"))
    except FileNotFoundError:
        pass  # No previous data, initialize empty list
    return transactions

# Function to save transactions to a file
def save_transactions(transactions):
    with open("transactions.txt", "w") as file:
        for transaction in transactions:
            file.write(f"{transaction.category},{transaction.amount},{transaction.is_expense}\n")

# Function to calculate total income and expenses
def calculate_totals(transactions):
    total_income = 0
    total_expense = 0
    for transaction in transactions:
        if transaction.is_expense:
            total_expense += transaction.amount
        else:
            total_income += transaction.amount
    return total_income, total_expense

# Function to analyze expenses by category
def analyze_expenses(transactions):
    expense_categories = {}
    for transaction in transactions:
        if transaction.is_expense:
            category = transaction.category
            expense_categories[category] = expense_categories.get(category, 0) + transaction.amount
    return expense_categories

def main():
    transactions = load_transactions()

    while True:
        print("\nBudget Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Analyze Expenses")
        print("4. Calculate Remaining Budget")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            transaction = get_transaction_info()
            transactions.append(transaction)
            save_transactions(transactions)
            print("Transaction added successfully!")
        elif choice == "2":
            if not transactions:
                print("No transactions found.")
            else:
                print("\nTransactions:")
                for transaction in transactions:
                    expense_type = "Expense" if transaction.is_expense else "Income"
                    print(f"{expense_type}: {transaction.category} - ${transaction.amount:.2f}")
        elif choice == "3":
            expense_categories = analyze_expenses(transactions)
            if not expense_categories:
                print("No expenses found to analyze.")
            else:
                print("\nExpense Analysis:")
                for category, amount in expense_categories.items():
                    print(f"{category}: ${amount:.2f}")
        elif choice == "4":
            total_income, total_expense = calculate_totals(transactions)
            remaining_budget = total_income - total_expense
            print(f"\nTotal Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Remaining Budget: ${remaining_budget:.2f}")
        elif choice == "5":
            save_transactions(transactions)
            print("Exiting Budget Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
