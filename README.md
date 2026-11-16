# Project-1-Personal-Finance-Tracker

# Personal Finance Tracker

A simple, dependency-free command-line application built in Python to help you track daily income and expenses, view your live balance, and save your financial history automatically.

## Tech Stack & Tools
- **Core Language:** Python 3 (Zero external dependencies)
- **Data Storage:** Python built-in `json` module (Local file serialization)
- **Environment & Workflow:** macOS Terminal (Zsh), VS Code, Git & GitHub

## How It Works
- **Interactive Menu:** Runs a continuous loop in your terminal so you can log transactions or check your history until you choose to exit.
- **Smart Input Validation:** Prevents crashes and bad data by checking that your entries match expected formats (e.g., strictly accepting `income` or `expense`).
- **Live Balance Calculation:** Loops through your stored records to add income and subtract expenses, displaying your up-to-date net balance.
- **Automatic Saving & Loading:** When you exit the app, all transactions are saved to a local `transactions.json` file. When you open the app again, your previous records load automatically.

## Getting Started

1. **Clone this repository** to your local machine:
   ```bash
   git clone [https://github.com/wilfb-debug/Project-1-Personal-Finance-Tracker.git](https://github.com/wilfb-debug/Project-1-Personal-Finance-Tracker.git)


Example usage: 

=== Personal Finance Tracker ===
1. Add Transaction
2. View Transactions
3. Exit
Select an option (1-3): 1
Enter amount ($): 300
Enter category (e.g., Food, Rent, Salary): salary
Enter type (income or expense): income

Success! Added income of $300.00 under 'salary'.
