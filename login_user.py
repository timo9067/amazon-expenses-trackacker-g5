import getpass

database = {"Federica", "TxelLci#2@8"}
user_name = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if user_name == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Welcome to Amazon")