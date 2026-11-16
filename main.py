import json

# 1. Storage for transaction records (list of dictionaries)
transactions = []

def add_transaction():
    amount = float(input("Enter amount ($): "))
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

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # If the file doesn't exist yet, start with an empty list

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
            with open("transactions.json", "w") as file:
                json.dump(transactions, file)
            print("Transactions saved. Goodbye!")   
            break
        else:
           print("Invalid selection. Please enter 1, 2, or 3.")

if __name__ == "__main__":
     main()
