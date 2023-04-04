# Backlog 

python3 amazon_expenses_tracker.py 


### 1. amazon_expenses_tracker.py 
Input from CL: 
- user_name: str (Optional)
- password: str (Optional)
This is the main programm

Output: 
- database of users
- database of purchases
- reports (template for generating reports, extracting data from `database of users` and `database of purchases`)

### 2. registration() -> users_db()

Input from `amazon_expenses_tracker()` or from `user` if was not inputed from CL: 
- user_name: str (optional) 
- password: str (optional)
- tel_number: str

Output: reg_success = True/False

### 3. login()
Input:
- user_name: str  
- password: str

Output: 
- login_successful: bool = True/False
- user_name: str
- phone_no: str


### 4. add_purchase() -> purchases_db()
Input from the user: 
    The date of the purchase (accept the following formats: MM/DD/YYYY, MM-DD-YYYY) but save the date as MM/DD/YYYY,
    The item purchased (should be a string of at least 3 characters),
    The total cost of the item (should be an integer or a float - including charges on devivery),
    The weight of the item( should be a float, and in kg)
    The quantity purchased (should be an integer from 1 and above).

Output: 
  purchases = {}
  
  d1 = { date_of_purchase: 02/23/2023,
    item: "book",
    total_cost: 25.88,
    weight: 2,
    quantity: 2
    }
    
    Formula: 
    total_cost = item_cost*quantity + weight*(1) 
    
  

### 5. report() 

Input:
 - purchases ={d1, d2, d3 ...}
 - user_name from login()
 - telephon_no from login ()

Output:
- Calculate the total charges for delivery. Amazon charges 1 EURO per 1 kg
- Calculate costs of the items, excluding delivery charges
- Calculate the most and least expensive orders
- Calculate the avarage cost with respect to the total number of orders
- Calculate if the user has exceeded a fixed speding limit e.g. 500 Euro.

