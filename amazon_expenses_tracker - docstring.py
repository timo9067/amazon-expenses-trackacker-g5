"""

   DCI Project "Amazon Expence Tracker"
   
   authors:
   Alina Ignat
   Fabricio Golino
   Swetlana König
   Timur Shakirov
   
   started: 04/01/2023
   
   project repository can be found here:
       
   https://github.com/timo9067/amazon-expenses-tracker-g5    
   
   modules and subroutines 
   =======================
   
   login.py 
   --------
   
   login(user_name, password)
   - validation of username and password
   - returns user_name, log_success (True or False)
   
   registration.py
   ---------------
   
   check_password(p) 
   - syntax check of password p
   - returns True of False
   
   registration_telnum() 
   - regex check german phonenumber 
   - returns a validated phonenumber
   
   registration(user_name, password)
   - check username and password
   - returns user_name, password, and sucess (True or False)
   
   add_purchase.py
   ---------------
   
   check_date(mydate)
   - is it a valid date?
   - get back True or False
   
   get_date(date_str)
   - usees check_date()
   - loop while date is not ok
   - returns a correct date
   
   add_purchase()
   - input and check date, item, cost, weight, quantity
   - returns a valid dictionary
   
   report.py
   ---------
   
   report()
   - print username, date and phonenumeber
   - print statistik
   - print spending limit info
   
   amazon_expenses_tracker.py - main program
   -----------------------------------------
   
   - parsing command line
   - checking user/password
   - initialising empty list for purchased items
   - menu - handle user input 1, 2, 3
   - quitting
   
"""

# importing python modules

import argparse
import sys
import os
import time

# importing group made modules

from add_purchase import add_purchase   # Sweta
from report       import report         # Fabrizio
from registration import registration   # Alina and Timur
from login        import login          # Alina and Timur

# our  functions
# def registration(user_name, password):
#     if user_name == "":
#         user_name = "Larry"
#     if password == "":
#         password = "GraT%DsT"
#     tel_number = "+49 154 155 11 11"
#     reg_success = True # can be False if something went wrong

#     return user_name, password, tel_number, reg_success

# def login(user_name, password):
#     if user_name == "": 
#         user_name = "Larry"
#     log_success = True # can be False if something went wrong
#     return user_name, log_success
    
# def add_purchase(purchases):
#    print("ADDING PURCHASE\n"*5)
    

# def report(purchases):
#     print("GENERATING REPORT\n"*10)



# parsing arguments from Command Line

parser = argparse.ArgumentParser(
    description="This program allows you to track your Amazon expenses"
)

parser.add_argument(
    "user_name",
    nargs="?",
    type=str,
    default="",
    help="User name for registration (optional)"
)
parser.add_argument(
    "password",
    nargs="?",
    type=str,
    default="",
    help="Password for registration (optional)"
)

args = parser.parse_args()

user_name = args.user_name
password = args.password

# clearing screen
os.system("clear")

# welcoming the user
logo = """
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
| AMAZON  PURCHASE TRACKING Utilility |
|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|
"""

print(logo)
print("This program allows to track your expenses on Amazon.")
print("Your registration will take just a few seconds.")

# passing the user_name and password to registration 

registred_user = registration(user_name, password)


# expecting return from function registration -> user_name, password, success

if registred_user[-1]: # checking if registration is successful
    user_name = registred_user[0] # updating user name
    password = registred_user[1] # updating password
    print("Congratulations! You are successfully registered!")
    print()
    print()
    
else:
    print()
    print("Sorry... Something went wrong with the registration. Please try again")
    print()
    sys.exit(1)
    
# passing user name and password to compare with user input

logged = login(user_name, password)

# checking if login was successful, last returned argument - success
if logged[-1]: 
    user_name = logged[0]
    if user_name in registred_user:  # this part is mostly for fututre to build multi-user environmnt
        tel_number = registred_user[2]
    else: 
        print("Sorry. No such user in our database") 
        sys.exit(1)
    
else: 
    print()
    print("Sorry... Something went wrong with the logging in. Please try again")
    print()
    sys.exit(1)


os.system("clear") 
print(f"Hello, {user_name}! Welcome to the Amazon Expense Tracker!")
menu_message = """
What would you like to do?
1. Enter a purchase
2. Generate a report
3. Quit"""

# generation empty list for dictionaries generated by add_purchase()
# the database  

purchases = []  

while True: 

    print(menu_message)
    user_choice = input("Enter your choice (1/2/3): ")

    match user_choice: 
        case "1":
            # Sweta
            os.system("clear")
            purchases.append(add_purchase()) 
        case "2": 
            # Fabricio
            os.system("clear")
            report(purchases, user_name, tel_number)
        case "3": 
            break
        case other:
            os.system("clear")
            print("Sorry. Operation entered is not valid. Please select from the available options")
            print()
            continue
        

# quitting

print()
print("Saving your data", end=".")

#printing dots 
for _ in range(10):
    time.sleep(0.2)
    print(".", end="", flush=True)
    
print()

print("Quitting program", end=".")

#printing dots 
for i in range(10):
    print(".", end="", flush=True)
    time.sleep(0.2)       

print()
    
