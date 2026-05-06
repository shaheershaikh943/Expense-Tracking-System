while True:
    try:
        Menu_Choice = int(input("1.Add Expense\n2.View Expenses\n3.Total Expense\n4.Search By Category\n5.Exit\nEnter Your Choice:"))
        break
    except Exception as e:
        print(f"Error:{e}")
if Menu_Choice == 1:            #Add Expenses
    with open(file="Expenses.txt",mode="a") as file:
        '''while True:
            try:
                times = int(input("Enter How often will you write down your expenses?:"))
                break
            except Exception as e:
                print(f"Error:{e}")
        for i in range(times):'''
        Date = input("Enter date: ")
        Category = input("Enter category: ")
        Amount = float(input("Enter amount(PKR): ")) 
        data = f"{Date},{Category},{Amount}\n"
        file.write(data)
elif Menu_Choice == 2:          #View Expenses
    with open(file="Expenses.txt",mode="r") as file:
        while True:
            try:
                Date = input("Enter the Date of Expense you want for analysis:")
                break
            except Exception as e:
                print(f"Error:{e}")
        for line in file.readlines():
            data = line.strip().split(",")
            if data[0] == Date:
                print(f"Date of Expense: {Date}\nCategory of Expense: {data[1]}\nAmount of Expense: {data[2]}")
                print()     #f"<{'-'*10}>"
elif Menu_Choice == 3:          #Total Expenses
    Total_Amount = 0
    with open(file="Expenses.txt",mode="r") as file:
        while True:
            try:
                Menu_Choice = int(input("1.By Date\n2.By Category\n3.Total of all Expenses\nSelect your desired option:"))
                break
            except Exception as e:
                print(f"Error:{e}")
        if Menu_Choice == 1:            #Total Expenses of a single day
            while True:
                try:
                    Date = input("Enter the Date of Expense you want for analysis:")
                    break
                except Exception as e:
                    print(f"Error:{e}")
            for line in file.readlines():
                data = line.strip().split(",")
                if data[0] == Date:
                    Amount = float(data[2])
                    #print(data[2])
                    #print(Amount)
                    Total_Amount = Total_Amount + Amount
            print(f"Total Expense spent on that date: {Total_Amount}")
        elif Menu_Choice == 2:            #Total Expenses of a single category
            while True:
                try:
                    Category = input("Enter the Date of Expense you want for analysis:")
                    break
                except Exception as e:
                    print(f"Error:{e}")
            for line in file.readlines():
                data = line.strip().split(",")
                if data[1] == Category:
                    Amount = float(data[2])
                    #print(data[2])
                    #print(Amount)
                    Total_Amount = Total_Amount + Amount
            print(f"Total Expense spent on that category: {Total_Amount}")
        elif Menu_Choice == 3:            #Total Expenses of All Entries
            for line in file.readlines():
                data = line.strip().split(",")
                Amount = float(data[2])
                    #print(data[2])
                    #print(Amount)
                Total_Amount = Total_Amount + Amount
            print(f"Total Expenses: {Total_Amount}")
        else:
            print("Invalid Choice")
elif Menu_Choice == 4:            #Search By Category
    with open(file="Expenses.txt",mode="r") as file:
        while True:
            try:
                Category = input("Enter the Category to search:")
                break
            except Exception as e:
                print(f"Error:{e}")
        for line in file.readlines():
            data = line.strip().split(",")
            if data[1] == Category:
                print(f"Date of Expense: {Category}\nCategory of Expense: {data[1]}\nAmount of Expense: {data[2]}")
                print()
elif Menu_Choice == 5:            #Exit the Program
    print("Exitting Program...")
    exit()
else:
    print("Invalid Choice!!!")