from datetime import datetime


def check_date(mydate):
    try:
        mydate = mydate.replace("-","/")
        mylist = mydate.split("/")
        if len(mylist[0]) < 2:
            return False
        if len(mylist[1]) < 2:
            return False
        # https://www.programiz.com/python-programming/datetime/strptime
        datetime.strptime(mydate, "%m/%d/%Y")
        return True
    except:
        return False

def get_date(date_str):
    # Check and correct if the input is not in MM/DD/YYYY format
    while not check_date(date_str):
        date_str = input("Invalid date format. Please enter the date of purchase in MM/DD/YYYY or MM-DD-YYYY format: ")
    return(date_str)


def add_purchase():
    # Initialize variables
    date = ""
    item = ""
    cost = 0.0
    weight = 0.0
    quantity = 0

    # Get user input for date and validate format
    date_str = input("Enter the date of purchase (MM/DD/YYYY or MM-DD-YYYY): ")
    date = get_date(date_str)

    # Get user input for item and validate length
    while len(item) < 3:
        item = input("Enter the item purchased (at least 3 characters): ")

    # Get user input for cost and validate type
    cost_valid = False
    while not cost_valid:
        cost_str = input("Enter the total cost of the item: ")
        if all(char.isdigit() or char == "." for char in cost_str):
            cost = float(cost_str)
            cost_valid = True
        else:
            print("Invalid input. Please enter a number.")

    # Get user input for weight and validate type
    weight_valid = False
    while not weight_valid:
        weight_str = input("Enter the weight of the item in kg: ")
        if all(char.isdigit() or char == "." for char in weight_str):
            weight = float(weight_str)
            weight_valid = True
        else:
            print("Invalid input. Please enter a number.")

    # Get user input for quantity and validate type and value
    quantity_valid = False
    while not quantity_valid:
        quantity_str = input("Enter the quantity purchased (1 or more): ")
        if quantity_str.isdigit() and int(quantity_str) >= 1:
            quantity = int(quantity_str)
            quantity_valid = True
        else:
            print(
                "Invalid input. Please enter a whole number greater than or equal to 1.")

    # Return the purchase information as a dictionary
    return {"date": date, "item": item, "cost": cost, "weight": weight, "quantity": quantity}
