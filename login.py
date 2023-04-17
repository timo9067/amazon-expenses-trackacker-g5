import time

def login(user_name, password):  
    
    fail_count = 0
    log_success = False
    fail_message = 'Invalid username or password'

    while fail_count <= 3: 
        if fail_count == 3: 
            print('Sorry, you have used 3 attempts. Please try again in a 5 seconds')
            for i in range (10): 
                time.sleep(0.5)
                print('.', end=' ', flush=True)
                fail_message = 'Sorry. You have exceeded the number of attempts to log in. Please try to register again'
            print()


        print("Please log in. Case sensitive.")  
        time.sleep(0.5)  
            
        print("Enter you Username, please")  
        entry = input(":>>>")  
        
        print("Input your Password.")  
        passentry = input(":>>>")  
        
        
        if entry == user_name and passentry == password:  
            print('Congratulations! You have logged in successfully!')
            print()
            log_success = True
            break
        else:  
            print(fail_message)
            print()
            fail_count +=1
    
    return user_name, log_success
