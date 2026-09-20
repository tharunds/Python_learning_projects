#we need inputs like alphabets,numbers etc
#we need computer to randomly choose from data
#we need to be aware of min no of digts used in passcode
#display the password 
#if its ok then we need to use it or again run a loop

import random 
import string
import time
data=list(string.ascii_letters + string.digits + string.punctuation)
def password_generator():
    while(1):
        new_data=(random.sample(data,8))
        suggested_password= "".join(new_data)
        print("password suggested :",suggested_password)
        print("If you agree with it replay with [YES] or else replay with [NO]")
        user_replay=input("enter your choice :")
        if ("yes"==user_replay.lower().strip()):
            print("your password is :",suggested_password)
            break
        elif ("no"==user_replay.lower().strip()):
            print("your new password is generating")
            time.sleep(3)
        else:
            print("invalid choice")

password_generator()



