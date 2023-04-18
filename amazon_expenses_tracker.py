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
   
   This program aims to help users track their Amazon expenses by providing a user-friendly platform for entering 
   details of each purchase, including the date, item, cost, quantity and weight. 
   With this data, the program will generate comprehensive reports that show the user's total spending on Amazon, 
   as well as the average cost of their purchases.
   
   This program can be started from the command line with the user's login name and password for registration, 
   like this: python3 amazon_expenses_tracker.py 'username' 'password'. If the user's password does not meet the 
   criteria for a valid password, the program will prompt the user to input a valid password. 
   If the program is started without login credentials, the program will prompt the user to input their username and password.

"""

#importing modules
import argparse
import sys
import os
import time

# importing group made modules
from add_purchase import add_purchase # Sweta
from report import report #Fabrizio
from registration import registration #Alina and Timur
from login import login #Alina and Timur

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
# the database (Sweta)

purchases = []  

while True: 

    print(menu_message)
    user_choice = input("Enter your choice (1/2/3): ")

    match user_choice: 
        case "1":
            # Sweta - module added
            os.system("clear")
            purchases.append(add_purchase()) # Sweta
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
    
