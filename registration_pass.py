import re


    
    
text = """ 
Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 characters long.
If the password is not valid the user will be ask to try again with a valid password, then exit the program."""

print(text)
p = input("Input your password:")
x = True
while x:  
    if (len(p)<6 or len(p)>20):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("\W",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Try again with a valid password")