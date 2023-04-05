from datetime import datetime

def get_date(date_str):
    # Check if the input is in MM/DD/YYYY format
    if "/" in date_str:
        # Convert the date to MM/DD/YYYY format
        formatted_date = date_str
    elif "-" in date_str:
        # Convert the date to MM/DD/YYYY format
        formatted_date = date_str.replace("-", "/")
    else:
        # Prompt user to re-enter the date in the correct format
        formatted_date = ""
        while True:
            try:
                formatted_date = datetime.strptime(input("Invalid date format. Please enter the date of purchase in MM/DD/YYYY or MM-DD-YYYY format: "), '%m/%d/%Y')
                break
            except ValueError:
                print("Invalid date format or date is not valid.")
        formatted_date = formatted_date.strftime('%m/%d/%Y')
    return formatted_date


def add_purchase(purchases):
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
    purchases.append( {"date": date, "item": item, "cost": cost, "weight": weight, "quantity": quantity} )
    
