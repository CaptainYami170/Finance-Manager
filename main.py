from finance_manager import FinanceManager
from report_generator import ReportGenerator

def main():
    finance_manager = FinanceManager()
    report_generator = ReportGenerator()

    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Add Savings")
        print("4. Generate Report")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = input("Enter income amount: ")
            source = input("Enter income source: ")
            date = input("Enter date (YYYY-MM-DD): ")
            finance_manager.add_income(amount, source, date)
        elif choice == '2':
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            finance_manager.add_expense(amount, category, date)
        elif choice == '3':
            amount = input("Enter savings amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            finance_manager.add_savings(amount, date)
        elif choice == '4':
            report_generator.generate_report()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
input(" ")
