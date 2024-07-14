from data_handler import DataHandler

class FinanceManager:
    def __init__(self):
        self.data_handler = DataHandler()

    def add_income(self, amount, source, date):
        self.data_handler.write_data(['income', amount, source, date])

    def add_expense(self, amount, category, date):
        self.data_handler.write_data(['expense', amount, category, date])

    def add_savings(self, amount, date):
        self.data_handler.write_data(['savings', amount, date])
