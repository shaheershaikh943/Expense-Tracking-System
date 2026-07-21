# <---------Functions--------->

# Add a new expense to the CSV file
def Add_Expenses():
     # Get expense details from the user
     expense_date = input("Enter the Date of Expense:")
     expense_category = input("Enter the Category of Expense:")
     expense_amount = float(input("Enter the amount of Expense:"))

     # Load existing expenses to generate a unique expense ID
     expense_data = View_Expenses()
     expense_id = f"Expense-{len(expense_data)+1}"

     # Save the new expense to the CSV file
     with open(file="Expense.csv", mode="a") as file:
          data = f"{expense_id},{expense_date},{expense_category},{expense_amount}\n"
          file.write(data)
          print("Expense Added Successfully!!!")


# Read and return all expense records from the CSV file
def View_Expenses():
    try:
        with open(file="Expense.csv", mode="r") as file:
            # Convert each line into a list by splitting at commas
            expense_data = [line.strip().split(",") for line in file.readlines()]
            return expense_data

    # Handle the case where the file does not exist
    except FileNotFoundError as e:
        print(f"{e}")
        return []

    # Handle any unexpected errors
    except Exception as e:
        print(f"{e}")
        return []


# Calculate and display the total amount of all expenses
def Total_Expense():
    expense_data = View_Expenses()
    total_expenses = 0

    # Add the amount of each expense
    for expense in expense_data:
            amount = float(expense[3])
            total_expenses += amount

    print(f"Total Expense : {total_expenses}")


# Search for an expense using its unique ID
def Search_By_id(expense_id):
    expense_data = View_Expenses()
    Found = False

    # Check each expense record for a matching ID
    for line in expense_data:
        if line[0] == expense_id:
            Found = True

            # Display the matching expense details
            print(f"""
                        Expense Id : {line[0]}
                        Date : {line[1]}
                        Category : {line[2]}
                        Amount : {line[3]}
                    """)

    # Display a message if no matching expense is found
    if not Found:
        print("Expense Id is not Registered!!!")


# <---------Functions--------->


# <---------Execution--------->

# Keep displaying the menu until the user exits
while True:

    # Ensure the user enters a valid menu choice
    while True:
        try:
            menu_choice = int(input(
                "1.Add Expense\n"
                "2.View Expenses\n"
                "3.Total Expense\n"
                "4.Search By expense_id\n"
                "5.Exit\n"
                "Enter Your Choice:"
            ))
            break

        # Handle invalid numeric input
        except Exception as e:
            print(f"Error:{e}")

    # Add a new expense
    if menu_choice == 1:
        Add_Expenses()

    # Display all stored expenses
    elif menu_choice == 2:
        view_expense = View_Expenses()
        for expense in view_expense:
            print(f"{expense}")

    # Display the total of all expenses
    elif menu_choice == 3:
        Total_Expense()

    # Search for an expense by its ID
    elif menu_choice == 4:
        Search_By_id(expense_id=input("Enter the Expense Id of Expense:"))

    # Exit the program
    elif menu_choice == 5:
        print("Exiting Program...")
        exit()

    # Handle invalid menu choices
    else:
        print("Invalid Entry!!!")

# <---------Execution--------->