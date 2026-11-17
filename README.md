# Personal Finance Tracker

A command-line personal finance app built in Python to help you log daily income and expenses, filter records by category or month, see spending totals, and save your data locally.

## Tech Stack & Tools
- **Core Language:** Python 3 (No external libraries required)
- **Data Storage & File Handling:** Python's built-in `json` and `pathlib` modules
- **Environment & Workflow:** macOS Terminal (Zsh), VS Code, Git & GitHub

## Project Structure
```text
Project-1-Personal-Finance-Tracker/
├── main.py           # Main menu loop, input checks, filtering, and balance/category calculations
├── storage.py        # Handles reading and writing data to transactions.json
├── transactions.json # Auto-generated local file that stores your saved transactions (gitignored)
├── .gitignore        # Keeps personal financial data (transactions.json) private and out of GitHub
└── README.md         # Project documentation

How It Works
	Interactive 5-Option Menu: Runs a loop in your terminal so you can add transactions, view or filter your history, check category totals, delete mistakes, or exit.

	Smart Input Validation & Suggestions: Stops the program from crashing if you type the wrong thing—it checks that amounts are positive numbers (try/except), blocks numbers-only or blank categories, suggests previously used categories as numbered shortcuts, and logs dates in DD-MM-YYYY format.

	Filtering, Live Balance & Category Summary: Uses list comprehensions to let you filter your ledger by category or month (MM-YYYY), calculates your net balance, and groups your total income and spending by category (like Food, Rent, or Salary).

	Auto-Saving & Safe Loading: Managed in storage.py, which loads your past transactions on startup (safely handling missing or empty files without crashing) and automatically saves your data every time you add or delete an entry.


Getting Started

1. Clone this repository to your local machine:

git clone [https://github.com/wilfb-debug/Project-1-Personal-Finance-Tracker.git](https://github.com/wilfb-debug/Project-1-Personal-Finance-Tracker.git)
cd Project-1-Personal-Finance-Tracker

2. Run the application:
python3 main.py


=== Personal Finance Tracker ===
1. Add Transaction
2. View Transactions
3. Category Summary
4. Delete Transaction
5. Exit
Select an option (1-5): 1
Enter amount: 240
Is this 'income' or 'expense'?: expense
Enter category (e.g., Food, Rent, Salary): Food
Enter date (DD-MM-YYYY) or press Enter for today: 17-11-2026

Success! Added and saved expense of 240.00 under 'Food' on 17-11-2026.
