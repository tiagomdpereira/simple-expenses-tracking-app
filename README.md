# Simple Expense Tracker

A command-line personal finance application for tracking daily expenses with budget management and categorization.

## Features

- **Add Expenses**: Record expenses with name, amount, category, and date
- **Expense Categories**: Organize expenses into predefined categories (Food, Home, Work, Entertainment, Other)
- **Budget Tracking**: Monitor spending against monthly budget with remaining balance
- **Expense Summary**: View spending breakdown by category and daily budget recommendations
- **Recent Expenses**: Display last N expenses for quick review
- **Remove Expenses**: Delete recent entries when needed

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd simple-expenses-tracking-app
```

2. Ensure Python 3.12+ is installed:
```bash
python --version
```

3. Run the application:
```bash
python expense_tracker.py
```

## Usage

Launch the application and choose from the menu options:

1. **Add Expense** - Enter expense details including amount, name, category, and date
2. **Remove Expense** - Delete the last N expenses
3. **Summarize Expenses** - View spending summary with budget analysis
4. **See Last Expenses** - Display recent expense entries
5. **Exit App** - Close the application

### Example

```
Running Expense Tracker!
Choose the action you want to perform.
1. Add Expense
2. Remove Expense
3. Summarize Expenses
4. See Last Expenses
5. Left App
Enter an action number (range from 1 - 5): 1

Getting User Expense
Enter expense amount: 25.50
Enter expense name: Lunch
Categories list:
1. Food
2. Home
3. Work
4. Entertainment
5. Other
Enter a category number (range from 1 - 5): 1
Date of the incurred expense in the format dd/mm/yyyy: 07/08/2025
```

## Data Storage

Expenses are stored in `expenses.csv` with the following format:
```
name,category,amount,day,month,year
```

## Requirements

- Python 3.12+
- No external dependencies required

## License

This project is open source and available under the MIT License.