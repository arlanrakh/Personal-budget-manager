# personal budget assistant



#creates class called BudgetManager
class BudgetManager():
# input option for income, expenses and other caregories regarding financial information 
    def __init__(self):
        self.income = []
        self.expenses = []
        self.categories = set()

# adding income based on user's input
    def add_income(self, amount):
        try: 
            self.income.append(float(amount))
        except ValueError:
            print("That wasn't an integer!")

# adding expense based on user's input (how much did he spend)
    def add_expenses(self, amount, category):
        try:
            amount = float(amount)
            self.expenses.append((amount, category))
            self.categories.add(category)
        except ValueError:
            print("That wasn't an integer!")

# displaying financial summary based on total income and expenses -> give us balance as a result      
    def show_finance_summary(self):
        total_income = sum(self.income)
        total_expenses = sum([expense[0] for expense in self.expenses])
        balance = total_income - total_expenses

# The "\nFinancial Summary" - financial summary is being printed
# other lines show total income, total expenses, and the balance.
# The "f" string format is used to insert the values of the variables into the strings.
# The ".2f" is used for that the values should be formatted as floating point numbers with two decimal places
# $ is used to convert them to money 
        print("\nFinancial Summary:")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Balance: ${balance:.2f}")


# This code checks if there are any expense categories in the list 
# If there are, it prints a header for the expenses by category
# Then for each category it calculates the total expense amount for that category and prints it formatted as a currency.
        if self.categories:
            print("\nExpenses by Category:")
            for category in self.categories:
                category_total = sum([expense[0] for expense in self.expenses if expense[1] == category])
                print(f"{category}: ${category_total:.2f}")



# This part defines a function named main
def main():
    manager = BudgetManager()

# It starts a loop that will continue infinitely unless stopped (also, i added some emojis)
    while True:
        print("\n ---WELCOME--- \U0001F468 Personal Budget Manager \U0001F468 ---WELCOME---")
        print("                      1. Add Income \U0001F4B5")
        print("                      2. Add Expense \U0001F4C9")
        print("                      3. Display Financial Summary \U0001F4B0")
        print("                      4. Exit \U0001F6AA")

        choice = input("\n Enter your choice: ")

# It checks the user's choice and does corresponding actions
        if choice == "1":
            amount = input("Enter the amount of income: ")
            manager.add_income(amount)
            if float(amount) >= 10000000:
                print("\n Damn, you are rich!")
        elif choice == "2":
            amount = input("Enter the amount of expense: ")
            category = input("Enter the expense category: ")
            manager.add_expenses(amount, category)
            if float(amount) >= 10000000:
                print("\n Wow, you spent a lot! Haha")
        elif choice == "3":
            manager.show_finance_summary()
        elif choice == "4":
            print("Exiting program. See you!")
            break
        else:
            print("Invalid choice. Please try again.")

# This part checks if the current script is being run as the main program
if __name__ == "__main__":
    main()
