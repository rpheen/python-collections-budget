from . import Expense

expenses = Expense.Expense(read_expenses(data/spending_data.csv))
spending_categories = []

for expense in expenses.list():
    spending_categories = append(expense.category)