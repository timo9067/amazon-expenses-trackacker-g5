import time  

LOGIN = ("Login", "login", "L", "l", "LOGIN")  
CREATE = ("Create", "create", "C", "c", "CREATE", "Create Account", "Create account", "create Account", "create account", "CREATE ACCOUNT")   
x = 0  
newPass = "X"  
newUser = "X"  

validEntry = {  
    "Larry" : "larrypass",  
    "Federica" : "federicapass"  
}  

print("--==Welcome==--")  
time.sleep(1)  
def choice():  
    print("Login or Create Account?")  
    choice = input(":>>>")  
    if choice in LOGIN:  
        login()  
    elif choice in CREATE:  
        create()           #Choice to login or create

def login():  
    print("""  
Please login. Case sensitive.""")  
    time.sleep(0.5)  
    print("Username.")  
    entry = input(":>>>")  
    if entry in validEntry:  
        x = 0  
        while x < 3:  
            print("Input Password.")  
            passentry = input(":>>>")  
            passright = validEntry.get(entry)  #Checks dictionary to find password associated with username entered
            if passentry == passright:  
                print("Successful Login!")     
                break 
            else:  
                print("""Incorrect password, try again  
                      """)  
                x += 1     #Incorrect password, allows three attempts 
    else:  
        print("Username not recognised!")  
        login()  

def create():  
    print("Please choose a username") 
    global newUser, newPass 
    newUser = str(input(":>>>"))  
    print("Please choose a password for", newUser)  
    newPass = str(input(":>>>"))  
     

choice()  

validEntry[newUser] = newPass #Adds new username and password to dictionary  

choice()  #You can only make one new account then login


    