from storage import load_transactions, save_transactions
from pathlib import Path

DATA_FILE = Path("transactions.json")

def load_transactions():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_transactions(transactions):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)

# Check if the transactions file exists
transaction_file = Path("transactions.json")
if transaction_file.exists():
    with open(transaction_file, "r") as file:
        transactions = json.load(file)
else:
    transactions = []

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

    category = input("Enter category (e.g., Food, Rent, Salary): ").strip()

    # Keep asking until they type a valid type 
    while True:
        trans_type = input("Enter type (income or expense): ").strip().lower()
        if trans_type in ["income", "expense"]:
            break
        print("Invalid type! Please type sctrictly 'income' or 'expense'.")

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

def display_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")

def main():
    global transactions
    transactions = load_transactions()

    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
           add_transaction()
        elif choice == "2":
           view_transactions()
        elif choice == "3":
            save_transactions(transactions)  
            print("Transactions saved. Goodbye!")   
            break
        else:
           print("Invalid selection. Please enter 1, 2, or 3.")

if __name__ == "__main__":
     main()
