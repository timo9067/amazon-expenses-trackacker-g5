# amazon-expenses-tracker-g5
Group project. Amazon expenses tracker


# Bunch of functions (files) to be written: 
### main() - main algorithm
### registration() -> users_db()
### login()
### add_purchase() -> purchases_db()
### report() 

### registration() -> users_db()
1. The program should accept username and password from the terminal for registration
2. Check the validity of the password using the following criteria:
    - Should have at least one number.
    - Should have at least one uppercase and one lowercase character.
    - Should have at least one special symbol.
    - Should be between 6 to 20 characters long. 
    - If the password is not valid the user will be ask to try again with a valid password, then exit the program. 
3. Ask the user to input his phone number(It should be a valid german mobile number). Prompt the user to input this number until he gets it right.


### login() - login if user registerd, if not - registration()

4. Ask the user to login. Print a message if the login was successful or print Invalid Username or password and ask again to enter username and password. If the user for three times input an incorrect username or password tell the user that he has used all the attempts and ask the user to try again after 5 seconds(Delay your app for 5 seconds). If after that 5 seconds he enters an incorrect username or password, ask the user to register again and exit the program. 
5. After the user has entered a valid password, he should be welcomed with the message ---> `Welcome to the Amazon Expense Tracker!`

### main()
6. Now you are ready to prompt user for input. A menu should be printed out showing 3 options: 
- `1. Enter a purchase`, 
- `2. Generate a report` (If this option is selected without entering any purchase, tell the user to enter at least one purchase and show the menu)
- `3. Quit.`
7. The user is asked to pick a choice using the numeric values associated. 

### add_purchase() -> purchases_db()
8. If the user picked `1`, the user should input 
   - The date of the purchase (accept the following formats: MM/DD/YYYY, MM-DD-YYYY) but save the date as MM/DD/YYYY, 
   - The item purchased (should be a string of at least 3 characters), 
   - The total cost of the item (should be an integer or a float - including charges on devivery), 
   - The weight of the item( should be a float, and in kg)
   - The quantity purchased (should be an integer from 1 and above).
9. If any of the condition for the inputs in step 8 is not met, prompt the user to re-enter the right value.

10. Save the purchases. Either in a list of dictionary(preferred).

Bonus> > You could enter multiple items in one session. 



### main()
11.  The user should be prompted again to the menu where he can choose `1` again if he needs to enter more items or he can choose other options.
12. If the user picked `2`, the script should generate a report: 
 

### report() 
12. If the user picked `2`, the script should generate a report: 
   - Calculate the total charges for delivery. Amazon charges `1 EURO` per `1 kg`
   - Calculate costs of the items, excluding delivery charges
   - Calculate the most and least expensive orders
   - Calculate the avarage cost with respect to the total number of orders
   - Calculate if the user has exceeded a fixed speding limit e.g. 500 Euro.
13. Finally print your report and when the report has been generated. (**hint** you can play with the the sleep() function here)


### main()
14. If the user picked `3`, the script should do nothing else, just print a goodbye message and quit. e.g. Display a final message thanking the user for the visit, using their name typed at the beginning.
15. If the user types anything different than `1`, `2` or `3` it should show an error message indicating the operation entered is not valid and instruct the user to select from the available options.


