import matplotlib.pyplot as plt
from data_handler import DataHandler

class ReportGenerator:
    def __init__(self):
        self.data_handler = DataHandler()

    def generate_report(self):
        data = self.data_handler.read_data()
        income, expenses, savings = 0, 0, 0
        expense_categories = {}

        for row in data:
            # Check if the row has the correct number of columns
            if len(row) < 3:
                print(f"Skipping malformed row: {row}")
                continue

            try:
                if row[0] == 'income':
                    income += float(row[1])
                elif row[0] == 'expense':
                    expenses += float(row[1])
                    if row[2] in expense_categories:
                        expense_categories[row[2]] += float(row[1])
                    else:
                        expense_categories[row[2]] = float(row[1])
                elif row[0] == 'savings':
                    savings += float(row[1])
            except ValueError as e:
                print(f"Error processing row: {row}")
                print(f"ValueError: {e}")

        print(f'Total Income: {income}')
        print(f'Total Expenses: {expenses}')
        print(f'Total Savings: {savings}')

        self.visualize_expenses(expense_categories)

    def visualize_expenses(self, expense_categories):
        categories = list(expense_categories.keys())
        amounts = list(expense_categories.values())
        plt.figure(figsize=(10, 5))
        plt.bar(categories, amounts, color='green')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.title('Expenses by Category')
        plt.show()
