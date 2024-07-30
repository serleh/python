from datetime import datetime
import pprint

# Function to add expense

def add_expense(expenses):
    category = input("Category ")
    des = input("Description")
    amount =input("Amount")
    date_input = input("Enter a date (YY-MM-DD)")
    # parse the input_date
    parsed_date = datetime.strptime(date_input,"%Y-%m-%d")
    expenses.append({"Category":category,"Description":des,"amount":amount,"Date":parsed_date})
    print("Expense added sucessfully")
    return expenses
    

# function to view all expense

def view_expenses(expenses):
    for expense in expenses:
        print(expense)
        return expense


def view_expenses_by_category(expenses,category):
    for expense in expenses:
        if expense['Category'] == category:
            print(expense)
   ## delete an expense based on a specific date     

def delete_expense(expenses,del_date):
    for expense in expenses:
        if expense['Date'] == del_date:
            expenses.remove(expense)
        print("Sucessfully removed")

def update_expense(expenses,description):
    for expense in expenses:
        if expense['Description']==description:
             category=input("Category")
             des = input("Description")
             amount =input("Amount")
             date_input = input("Enter a date (YY-MM-DD)")
                # parse the input_date
             parsed_date = datetime.strptime(date_input,"%Y-%m-%d")
             expenses.append({"Category":category,"Description":des,"amount":amount,"Date":parsed_date})
             print("Expense Updated sucessfully")
             return expenses


def main():
    expenses=[]
    while True:
        print("\nYOUR RELIABLE EXPENSE TRACKER")
        print("1. Add expense")
        print("2. View all expenses")
        print("3. View all expense by category")
        print("4. Delete an expense")
        print("5. Update an expense")
        print("6. Calculate total expenses")




        choice = input("Enter a number")


        if choice =="1":
           add_expense(expenses)
        elif choice=='2':
            view_expenses(expenses)
        elif choice=="3":
            category = input("Enter Category you want to search")
            view_expenses_by_category(expenses, category)
        elif choice=="4":
            del_date = input("Enter a date (YY-MM-DD)")
           # parse the input_date
            parsed_date = datetime.strptime(del_date,"%Y-%m-%d")
            delete_expense(expenses,del_date)
        elif choice=='5':
            description=input("enter the description of the app you want to update")
            update_expense(expenses,description)

 

if __name__ == "__main__":
    main()