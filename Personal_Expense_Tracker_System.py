# <---------Functions--------->

def Add_Expenses():
     expense_date = input("Enter the Date of Expense:")
     expense_category = input("Enter the Category of Expense:")
     expense_amount = float(input("Enter the amount of Expense:"))
     expense_data = View_Expenses()
     expense_id = f"Expense-{len(expense_data)+1}"
     with open(file="Expense.csv",mode="a") as file:
          data = f"{expense_id},{expense_date},{expense_category},{expense_amount}\n"
          file.write(data)
          print("Expense Added Successfully!!!")

def View_Expenses():
    try:
        with open(file="Expense.csv",mode="r") as file:
            expense_data = [line.strip().split(",") for line in file.readlines()]
            return expense_data
    except FileNotFoundError as e:
        print(f"{e}")
        return []
    except Exception as e:
        print(f"{e}")
        return []

def Total_Expense():
    expense_data = View_Expenses()
    total_expenses = 0
    for expense in expense_data:
            amount = float(expense [3])
            total_expenses += amount
    print(f"Total Expense : {total_expenses}")

def Search_By_id(expense_id):
    expense_data = View_Expenses()
    Found = False
    for line in expense_data:
        if line [0] == expense_id:
            Found = True
            print(f"""
                        Expense Id : {line[0]}
                        Date : {line[1]}
                        Category : {line[2]}
                        amount : {line[3]}
                    """)
                
    if not Found:
        print("Expense Id is not Registered!!!")

# <---------Functions--------->

# <---------Execution--------->

while True:
    while True:
        try:
            menu_choice = int(input("1.Add Expense\n2.View Expenses\n3.Total Expense\n4.Search By expense_id\n5.Exit\nEnter Your Choice:"))
            break
        except Exception as e:
            print(f"Error:{e}")
    if menu_choice == 1:
        Add_Expenses()
    elif menu_choice == 2:
        view_expense = View_Expenses()
        for expense in view_expense:
            print(f"{expense}")
    elif menu_choice == 3:
        Total_Expense()
    elif menu_choice == 4:
        Search_By_id(expense_id = input("Enter the Expense Id of Expense:"))
    elif menu_choice == 5:
        print("Exiting Program...")
        exit()
    else:
        print("Invalid Entry!!!")

# <---------Execution--------->