from expense import Expense
from datetime import datetime
import calendar


def main():
    print("Running Expense Tracker!")

    file_path = "expenses.csv"
    budget = 1000

    # let the user choose the action
    actions: list[str] = [
        "Add Expense",
        "Remove Expense",
        "Summarize Expenses",
        "See Last Expenses",
        "Left App"
    ]
    
    while True:
        # user has to insert a valid action
        while True:
            print("Choose the action you want to perform.")
            for i, action in enumerate(actions):
                print(f"{i + 1}. {action}")
            action_index: int = int(input(f"Enter an action number (range from 1 - {len(actions)}): ")) - 1
            if action_index in range(len(actions)):
                break
            else:
                print("Invalid Action Number.")
        
        action: str = actions[action_index]

        print("\n")

        # complete the action that the user chose.
        match action:
            case "Add Expense":

                while True:
                # Get user input
                    expense: Expense = get_user_expense()

                    # write their expense to a file
                    save_expense_to_file(expense, file_path)
                
                    print("Do you want to add more expenses?")
                    answers: list[str] = ["y", "n"]

                    while True: # get answer and check for a valid one
                        answer: str = input("Answer (y or n): ")
                        if answer in answers:
                            break
                        else:
                            print("Invalid Answer.")
                    
                    if answer == 'n':
                        break

            case "Remove Expense":
                remove_expenses(file_path)

            case "Summarize Expenses":
                # summarize expenses
                summarize_expenses(file_path, budget)
            
            case "See Last Expenses":
                get_last_expenses(file_path)

            case "Left App":
                print("Manage your finances wisely!")
                break
    
        print("\n")


def get_user_expense() -> Expense:

    print("Getting User Expense")

    expense_amount: float = float(input("Enter expense amount: "))
    expense_name: str = input("Enter expense name: ")

    expense_categories: list[str] = [
        "Food",
        "Home",
        "Work",
        "Entertainment",
        "Other"
    ]

    while True:
        print("Categories list:")
        for i, category in enumerate(expense_categories): # show category list
            print(f"{i + 1}. {category}")

        expense_index: int = int(input(f"Enter a category number (range from 1 - {len(expense_categories)}): ")) - 1
        if expense_index in range(len(expense_categories)):
            break
        else:
            print("Invalid Category Number.")
        
    expense_category: str = expense_categories[expense_index]

    while True:
        try:
            expense_date: str = input("Date of the incurred expense in the format dd/mm/yyyy: " )
            expense_datetime = datetime.strptime(expense_date, '%d/%m/%Y')
            break
        except:
            print("Invalid date format.")


    new_expense: Expense = Expense(expense_name, expense_category, expense_amount, expense_datetime)

    print("Expense created", new_expense)

    return new_expense


def save_expense_to_file(expense: Expense, expense_file_path: str) -> None:
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount},{expense.date.day},{expense.date.month},{expense.date.year}\n")
    print("Saving User Expense")


def summarize_expenses(file_path: str, budget: float):
    print("Summarizing User Expenses")
    expenses: list[Expense] = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line: str = line.strip()
            expense_name, expense_category, expense_amount, expense_day, expense_month, expense_year = stripped_line.split(",")
            line_expense: Expense = Expense(expense_name, expense_category, float(expense_amount), datetime(int(expense_year), int(expense_month), int(expense_day)))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        amount_by_category[key] = amount_by_category.get(key, 0) + expense.amount
    
    # show expenses by category
    print("Expenses By Category")
    for category, amount in amount_by_category.items():
        print(f"    {category}: €{amount:.2f}")
    
    # show total spent
    total_spent: int = 0
    for expense in expenses:
        total_spent += expense.amount
    print(f"Total spent: €{total_spent:.2f}")

    # show remaining budget
    remaining_budget = budget - total_spent
    print(f"Remaining budget: €{remaining_budget:.2f}")

    # show how much we have to spend per day
    now: datetime = datetime.now()
    days_in_month: int = calendar.monthrange(now.year, now.month)[1]
    days_left_in_month = days_in_month - now.day
    print(f"Remaining days in the current month: {days_left_in_month}")
    remaining_daily_budget = remaining_budget / days_left_in_month
    print(f"Remaining budget per day until the end of the month: €{remaining_daily_budget:.2f}")


def get_last_expenses(file_path: str) -> None:
    """
    x is the number of the last expenses the user want to read
    """
    x = int(input("Number of the last rows you want to see: "))
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines[-x:]:
            stripped_line: str = line.strip()
            expense_name, expense_category, expense_amount, expense_day, expense_month, expense_year = stripped_line.split(",")
            print(f"<{expense_name}, {expense_category}, {expense_amount}, {expense_day.zfill(2)}/{expense_month.zfill(2)}/{expense_year}>")


def remove_expenses(file_path: str) -> None:
    x = int(input("Number of the last expenses you want to remove: "))

    with open(file_path, "r") as f:
        lines = f.readlines()
        new_lines = lines[:-x]
    
    with open(file_path, "w") as f:
        for line in new_lines:
            f.write(line)
    
    print(f"Last {x} expenses were removed.")


if __name__ == "__main__":
    main()
