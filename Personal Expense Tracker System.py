# <---------Functions--------->

def Add_Expenses():
     expense_date = input("Enter the Date of Expense:")
     expense_category = input("Enter the Category of Expense:")
     expense_amount = float(input("Enter the amount of Expense:"))
     expense_data = View_Expenses()
     id = f"Expense-{len(expense_data)+1}"
     with open(file="Expenses.txt",mode="a") as file:
          data = f"{id},{expense_date},{expense_category},{expense_amount}\n"
          file.write(data)

def View_Expenses():
    try:
        with open(file="Expenses.txt",mode="r") as file:
            expense_data = [line.strip().split(",") for line in file.readlines()]
            return expense_data
    except FileNotFoundError:
        return []
    except Exception as e:
        return []

def Total_Expense():
    expense_data = View_Expenses()
    total_expenses = 0
    for i in range(len(expense_data)):
        amount = expense_data [i][3]
        total_expenses += amount
        print(f"Total Expense : {total_expenses}")

def Search_By_id(id):
    expense_data = View_Expenses()
    for line in expense_data:
        if line [0] == id:
            print(f"id : {line[0]}")
            print(f"Date : {line[1]}")
            print(f"Category : {line[2]}")
            print(f"amount : {line[3]}")
    else:
        print("id is not Registered!!!")

# <---------Functions--------->

# <---------Execution--------->

while True:
    while True:
        try:
            menu_choice = int(input("1.Add Expense\n2.View Expenses\n3.Total Expense\n4.Search By id\n5.Exit\nEnter Your Choice:"))
            break
        except Exception as e:
            print(f"Error:{e}")
    if menu_choice == 1:
        Add_Expenses()
    elif menu_choice == 2:
        view_expense = View_Expenses()
        print(f"View_Expense")
    elif menu_choice == 3:
        Total_Expense()
    elif menu_choice == 4:
        Search_By_id(id = input("Enter the id of Expense:"))
    elif menu_choice == 5:
        print("Exiting Program...")
        exit()
    else:
        print("Invalid Entry!!!")

# <---------Execution--------->