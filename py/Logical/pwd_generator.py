#This program will generate you a secure password from a base lenght of its.
import random as random
def generate_pwd(security):
    password = ""
    try:
        if security is 1: 
            for i in range(8):
                password += chr(random.randint(48, 57)) #Taking just numbers from ASCII code
        if security is 2:
            for i in range(16):
                password += chr(random.randint(48, 126)) #Taking letters and numbers from ASCII code
        if security is 3:
            for i in range(32):
                password += chr(random.randint(32, 126)) #Taking letters, numbers and symbols from ASCII code
    except:
        pass
    
    return password

print("Your new password is -> " + generate_pwd(int(input("Enter security level (choose a number):\n 1.Safe\n 2.Strict\n 3.Anti hackers\n"))))