# Program: Expense Tracker

# Create here an empty list to store all expense details
expenses = []

# Keep asking for expenses until user types 'exit'
while True:
    # it will Ask for expense name like food,rent, diet
    item = input("Enter expense name (or type 'exit' to finish): ")

    # loop  will stop here if user types 'exit'
    if item.lower() == 'exit':
        break

    while True:  # loop until a valid number is entered
        cost_input = input("Enter cost for " + item)
        cost_input = cost_input.replace(",", "")  # REMOVE commas
        try:
            cost = float(cost_input)  # convert string to float
            break  # exit loop if successful
        except ValueError:
            print("Invalid input! Please enter a number without letters or symbols.")

    # Add expense to the list as a dictionary
    expenses.append({'item': item, 'cost': cost})
    print("Added: " + item + " - ₹" + str(cost) + "\n")  # confirmation

# Calculation of total expenses
total = sum(exp['cost'] for exp in expenses)

# Show expense summary
print("\n=== Expense Summary ===")
for exp in expenses:
    print(exp['item'] + ": ₹" + str(exp['cost']))

# here will see total expense
print("\nTotal Expense: ₹" + str(total))
