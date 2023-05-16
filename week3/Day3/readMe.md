Expense Tracker

This code implements an Expense Tracker program that allows users to track their expenses, view reports, and manage their budget. The Expense Tracker uses a class called ExpenseTracker to manage expenses and perform various operations.

The ExpenseTracker class is defined with the following methods:

__init__: Initializes the expenses list and categories set.
add_expense: Adds a new expense to the tracker with the specified category, amount, and current date.
view_expenses: Displays all the expenses in the tracker.
view_category_spending: Displays the total spending for each category.
view_overall_spending: Displays the total spending across all categories.
view_total_savings: Calculates and displays the total savings based on the provided income.
generate_monthly_report: Generates a report for a specific month and year, including total spending and category spending.
generate_annual_report: Generates an annual report for a specific year, including total spending and category spending.
suggest_budget: Suggests budgets for each category based on average spending.
save_expenses_to_file: Saves the expenses to a CSV file.
load_expenses_from_file: Loads expenses from a CSV file.
The main function is defined to create an instance of the ExpenseTracker class and present a menu for users to interact with the Expense Tracker. The menu options include adding expenses, viewing expenses, generating reports, suggesting budgets, saving expenses to a file, loading expenses from a file, and exiting the program.

Inside the main function, user input is used to determine the selected menu option, and the corresponding method of the ExpenseTracker class is called.

The program continues to display the menu until the user chooses to exit by selecting option 11.

This code provides a basic framework for an Expense Tracker program, allowing users to track their expenses, view reports, and manage their budget. Users can add, view, and analyze their expenses, as well as save and load expense data from files.