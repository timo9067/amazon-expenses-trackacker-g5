def report(purchases, user_name, tel_number):
    # Check if the list of purchases is empty
    if not purchases:
        print("No purchase to report, please enter it first")
        return
    # Calculate total delivery charges
    total_delivery_charges = sum(purchase["weight"] for purchase in purchases)
    total_delivery_charges *= 1  # Amazon charges 1 EURO per 1 kg

    # Calculate total item costs
    total_item_cost = sum(purchase["cost"] for purchase in purchases)

    # Find most and least expensive orders
    most_expensive = max(purchases, key=lambda x: x["cost"])
    least_expensive = min(purchases, key=lambda x: x["cost"])

    # Calculate average cost per order
    num_orders = len(purchases)
    avg_cost_per_order = total_item_cost / num_orders

    # Calculate purchase date range
    purchase_dates = [purchase["date"] for purchase in purchases]
    purchase_date_range = f"{min(purchase_dates)} to {max(purchase_dates)}"

    # Mask phone number with asterisks
    masked_tel_number = tel_number[:3] + "***" + tel_number[-2:]

    # Check if spending limit exceeded
    spending_limit = 500
    total_spent = total_item_cost + total_delivery_charges
    if total_spent > spending_limit:
        note = "Note: You have exceeded the spending limit of 500 EURO"
    else:
        note = "Note: You have not exceeded the spending limit of 500 EURO"

    # Print report
    print("-------------------------")
    print("| Amazon Expense Report |")
    print("-------------------------")
    print(
        f"name: {user_name}    password: ***      Tel: +49{masked_tel_number}      Date: {purchases[0]['date']}")
    print("----------------------------------")
    print(f"DELIVERY CHARGES       TOTAL ITEM COST             ")
    print(
        f"  {total_delivery_charges:.2f} EURO                 {total_item_cost:.2f} EURO  ")
    print("  ")
    print("MOST EXPENSIVE        LEAST EXPENSIVE")
    print(
        f"name: {most_expensive['item']}            name: {least_expensive['item']}")
    print(
        f"cost: {most_expensive['cost']:.2f} EURO          cost: {least_expensive['cost']:.2f} EURO")
    print("  ")
    print(f"AVERAGE COST OF ITEM PER ORDER: {avg_cost_per_order:.2f} EURO")
    print(f"PURCHASE DATE RANGE: {purchase_date_range}")
    print("--------")
    print(note)

