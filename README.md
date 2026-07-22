# Expense Tracking System

A simple command-line **Personal Expense Tracker** built in Python. It lets you add, view, total, and search your daily expenses, with all records stored persistently in a CSV file — no database or external dependencies required.

## Features

- **Add Expense** — Record a new expense with a date, category, and amount. Each entry is automatically assigned a unique ID (`Expense-1`, `Expense-2`, ...).
- **View Expenses** — List every expense that has been recorded so far.
- **Total Expense** — Calculate and display the sum of all recorded expenses.
- **Search by Expense ID** — Look up a specific expense and view its full details.
- **Persistent Storage** — All expenses are saved to a CSV file, so your data is kept between runs.

## Tech Stack

- **Language:** Python 3 (standard library only — no external packages required)
- **Storage:** CSV file (`Expense.csv`)

## Project Structure

```
Expense-Tracking-System/
├── Personal_Expense_Tracker_System.py   # Main application script
└── Expense.csv                          # Auto-generated/updated file storing expense records
```

## Getting Started

### Prerequisites

- Python 3.x installed on your machine

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shaheershaikh943/Expense-Tracking-System.git
   cd Expense-Tracking-System
   ```
2. Run the script:
   ```bash
   python Personal_Expense_Tracker_System.py
   ```

No additional installation or setup is required — the script uses only Python's built-in libraries.

## Usage

When you run the script, you'll see a simple menu:

```
1.Add Expense
2.View Expenses
3.Total Expense
4.Search By expense_id
5.Exit
Enter Your Choice:
```

- **Option 1:** Enter a date, category, and amount to log a new expense.
- **Option 2:** Prints all stored expenses as raw records.
- **Option 3:** Prints the running total of every expense recorded.
- **Option 4:** Enter an expense ID (e.g. `Expense-1`) to view that entry's details.
- **Option 5:** Exits the program.

### Example Record Format

Each row in `Expense.csv` follows this structure:

```
Expense-1,12 May 2026,Food,1120.76
Expense-2,04 May 2026,Travel,11200.76
```

`expense_id, date, category, amount`

## Error Handling

The script gracefully handles:
- Missing CSV file on first run (starts with an empty expense list)
- Invalid/non-numeric menu input
- Searching for an expense ID that doesn't exist

## Future Improvements

Some ideas for extending this project:
- Edit or delete existing expenses
- Filter/sort expenses by date or category
- Export summary reports (e.g. monthly totals)
- Migrate storage to SQLite for more robust querying
- Add a simple GUI or web front end

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repo and submit a pull request.

## License

This project currently has no license specified. Consider adding one (e.g. MIT) if you plan to share or accept contributions.