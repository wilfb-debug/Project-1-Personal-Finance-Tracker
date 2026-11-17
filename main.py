from storage import load_transactions, save_transactions

transactions = load_transactions()

def add_transaction():
    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount <= 0:
                print("Amount must be greater than $0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 50 or 12.50).")

    while True:
        category = input("Enter category (e.g., Food, Rent, Salary): ").strip()
        if category:
            break
        print("Category cannot be blank. Please enter a category.")

    # Keep asking until they type a valid type 
    while True:
        trans_type = input("Enter type (income or expense): ").strip().lower()
        if trans_type in ["income", "expense"]:
            break
        print("Invalid type! Please type strictly 'income' or 'expense'.")

    transaction = {
    	"amount": amount,
    	"category": category,
    	"type": trans_type, 
        }

    transactions.append(transaction)
    print(f"\nSuccess! Added {trans_type} of ${amount:.2f} under '{category}'.")

def view_transactions():
    balance = 0.0 

    if len(transactions) == 0:
        print("No transactions found.")
    else:
        print("\n--- All Transactions ---")
        for transaction in transactions:
            print(
                f"{transaction['type'].capitalize()}: ${transaction['amount']:.2f} - Category: {transaction['category']}"
            )      

            if transaction["type"] == 'income':
                balance += transaction['amount']
            else:
                balance -= transaction['amount']

# 2. 
    print(f"\nCurrent Balance: ${balance:.2f}")

def category_summary():
    if not transactions:
        print("No transactions found.")
        return

    income_totals = {}
    expense_totals = {}

    for transaction in transactions:
        category = transaction["category"].capitalize()
        amount = transaction["amount"]

        if transaction["type"] == "income":
            income_totals[category] = income_totals.get(category, 0.0) + amount
        else:
            expense_totals[category] = expense_totals.get(category, 0.0) + amount

    print("\n--- Summary by Category ---")
    if income_totals:
        print("Income:")
        for category, total in income_totals.items():
            print(f"  {category}: +${total:.2f}")

    if expense_totals:
        print("Expenses:")
        for category, total in expense_totals.items():
            print(f"  {category}: -${total:.2f}")

def display_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Category Summary")
    print("4. Exit")

def main():
    global transactions
    transactions = load_transactions()

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            save_transactions(transactions)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
     main()
