from storage import load_transactions, save_transactions
from datetime import datetime
transactions = load_transactions()

def add_transaction():
    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount <= 0:
                raise ValueError("Amount must be greater than $0.")
            break
        except ValueError as e:
            print(f"Invalid input! {e} Please enter a positive number (e.g., 50 or 12.50).")

    # Gather unique previously used categories (preserving order)
    existing_categories = list(dict.fromkeys(t["category"].capitalize() for t in transactions))

    while True:
        if existing_categories:
            print("\nPrevious categories:")
            for idx, cat in enumerate(existing_categories, start=1):
                print(f"  {idx}. {cat}")
            cat_input = input("Pick a number above or type a new category: ").strip()

            if cat_input.isdigit():
                choice_idx = int(cat_input) - 1
                if 0 <= choice_idx < len(existing_categories):
                    category = existing_categories[choice_idx]
                    break
                else:
                    print("Invalid number. Pick a number from the list or type a new category.")
                    continue
        else:
            cat_input = input("Enter category (e.g., Food, Rent, Salary): ").strip()

        if not cat_input:
            print("Category cannot be blank. Please enter a category.")
        elif not any(char.isalpha() for char in cat_input):
            print("Invalid category! Please enter a text name (e.g., Food, Rent), not just numbers.")
        else:
            category = cat_input.capitalize()
            break

    while True:
        trans_type = input("Enter type (income or expense): ").strip().lower()
        if trans_type in ["income", "expense"]:
            break
        print("Invalid type! Please type strictly 'income' or 'expense'.")

    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    date_str = date_input if date_input else datetime.now().strftime("%Y-%m-%d")

    transaction = {
        "amount": amount,
        "category": category,
        "type": trans_type,
        "date": date_str,
    }

    transactions.append(transaction)
    save_transactions(transactions)  # Auto-save immediately!
    print(f"\nSuccess! Added and saved {trans_type} of ${amount:.2f} under '{category}' for {date_str}.")

def view_transactions():
    if not transactions:
        print("No transactions found.")
        return

    print("\nFilter options: [A]ll | [C]ategory | [M]onth (YYYY-MM)")
    filter_choice = input("Choose filter (press Enter for All): ").strip().lower()

    if filter_choice == "c":
        target_cat = input("Enter category to filter by: ").strip().lower()
        filtered = [t for t in transactions if t["category"].lower() == target_cat]
    elif filter_choice == "m":
        target_month = input("Enter month (YYYY-MM, e.g., 2026-11): ").strip()
        filtered = [t for t in transactions if t.get("date", "").startswith(target_month)]
    else:
        filtered = [t for t in transactions]

    if not filtered:
        print("No matching transactions found.")
        return

    balance = 0.0
    print("\n--- Filtered Transactions ---")
    for t in filtered:
        date_display = t.get("date", "N/A")
        print(f"[{date_display}] {t['type'].capitalize()}: ${t['amount']:.2f} - Category: {t['category']}")
        if t["type"] == "income":
            balance += t["amount"]
        else:
            balance -= t["amount"]

    print(f"\nFiltered Net Balance: ${balance:.2f}")

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

def delete_transaction():
    if not transactions:
        print("No transactions to delete.")
        return

    print("\n--- Select a Transaction to Delete ---")
    for idx, t in enumerate(transactions, start=1):
        date_display = t.get("date", "N/A")
        print(f"{idx}. [{date_display}] {t['type'].capitalize()}: ${t['amount']:.2f} - {t['category']}")

    while True:
        choice = input("\nEnter the number to delete (or 'c' to cancel): ").strip().lower()
        if choice == "c":
            print("Deletion cancelled.")
            return
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(transactions):
                removed = transactions.pop(idx)
                save_transactions(transactions)  # Auto-save immediately!
                print(f"Deleted: {removed['type'].capitalize()} of ${removed['amount']:.2f} ({removed['category']}).")
                return
        print(f"Invalid selection. Enter a number between 1 and {len(transactions)}, or 'c' to cancel.")

def display_menu():
    print("\n=== Personal Finance Tracker ===")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Category Summary")
    print("4. Delete Transaction")
    print("5. Exit")

def main():
    global transactions
    transactions = load_transactions()

    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            delete_transaction()
        elif choice == "5":
            save_transactions(transactions)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
     main()
