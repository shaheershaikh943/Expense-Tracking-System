# <---------Functions--------->

def Add_Expenses():
     Expense_Date = input("Enter the Date of Expense:")
     Expense_Category = input("Enter the Category of Expense:")
     Expense_Amount = input("Enter the Amount of Expense:")
     Expense_Data = View_Expenses()
     ID = f"Expense-{len(Expense_Data)+1}"
     with open(file="Expenses.txt",mode="a") as file:
          Data = f"{ID},{Expense_Date},{Expense_Category},{Expense_Amount}\n"
          file.write(Data)

def View_Expenses():
    try:
        with open(file="Expenses.txt",mode="r") as file:
            Expense_Data = [line.strip().split(",") for line in file.readlines()]
            return Expense_Data
    except FileNotFoundError:
        return []
    except Exception as e:
        return []

def Total_Expense():
    Expense_Data = View_Expenses()
    Total_Expenses = 0
    for i in range(len(Expense_Data)):
        Amount = Expense_Data [i][3]
        Total_Expenses += Amount
        print(f"Total Expense : {Total_Expenses}")

def Search_By_ID(ID):
    Expense_Data = View_Expenses()
    for line in Expense_Data:
        if line [0] == ID:
            print(f"ID : {line[0]}")
            print(f"Date : {line[1]}")
            print(f"Category : {line[2]}")
            print(f"Amount : {line[3]}")
    else:
        print("ID is not Registered!!!")

# <---------Functions--------->

# <---------Execution--------->

while True:
    while True:
        try:
            Menu_Choice = int(input("1.Add Expense\n2.View Expenses\n3.Total Expense\n4.Search By ID\n5.Exit\nEnter Your Choice:"))
            break
        except Exception as e:
            print(f"Error:{e}")
    if Menu_Choice == 1:
        Add_Expenses()
    elif Menu_Choice == 2:
        View_Expense = View_Expenses()
        print(f"View_Expense")
    elif Menu_Choice == 3:
        Total_Expense()
    elif Menu_Choice == 4:
        Search_By_ID(ID = input("Enter the ID of Expense:"))
    elif Menu_Choice == 5:
        print("Exiting Program...")
        exit()
    else:
        print("Invalid Entry!!!")

# <---------Execution--------->