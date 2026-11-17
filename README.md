# Personal Finance Tracker

A command-line personal finance app built in Python to help you log daily income and expenses, see spending totals by category, and save your data locally.

## Tech Stack & Tools
- **Core Language:** Python 3 (No external libraries required)
- **Data Storage & File Handling:** Python's built-in `json` and `pathlib` modules
- **Environment & Workflow:** macOS Terminal (Zsh), VS Code, Git & GitHub

## Project Structure
```text
Project-1-Personal-Finance-Tracker/
├── main.py           # Main menu loop, input checks, and balance/category calculations
├── storage.py        # Handles reading and writing data to transactions.json
├── transactions.json # Auto-generated file that stores your saved transactions
└── README.md         # Project documentation

## How It Works
Interactive Menu: Runs a loop in your terminal so you can keep adding transactions, view your history, check category totals, or save and exit.

Smart Input Validation: Stops the program from crashing if you type the wrong thing—it checks that amounts are positive numbers (try/except), blocks blank categories, and only accepts income or expense.

Live Balance & Category Summary: Loops through your saved transactions to calculate your current balance and groups your total income and spending by category (like Food, Rent, or Salary).

Safe Saving & Loading: Managed in storage.py, which loads your past transactions when the app starts (and safely handles missing or empty files without crashing) and saves everything when you exit.



##Getting Started
1. Clone this repository to your local machine:

git clone [https://github.com/wilfb-debug/Project-1-Personal-Finance-Tracker.git](https://github.com/wilfb-debug/Project-1-Personal-Finance-Tracker.git)
cd Project-1-Personal-Finance-Tracker

2. Run the application:

python3 main.py


Example Usage


=== Personal Finance Tracker ===
1. Add Transaction
2. View Transactions
3. Category Summary
4. Exit
Select an option (1-4): 1
Enter amount ($): 300
Enter category (e.g., Food, Rent, Salary): salary
Enter type (income or expense): income

Success! Added income of $300.00 under 'salary'.
