#range of numbers
#computer randomly choose  and stored
#user should guess no
#we should suggest whether guess no is near or not
#so we need to create loop
#display the result

import random
x=int(input("enter the minimum value : " ))
y=int(input("enter the maximum value:"))

original_num=random.randint(x,y)
print(original_num)
def guess_the_num():
     while(1):
         guess=int(input("guess the number :"))
         if (guess>original_num):
             print("your guess is  high")
         elif (guess<original_num):
             print("your guess is low")
         elif(guess==original_num):
             print("your guess is correct")
             print("congratulation")
             break
         else:
             print("enter the valid number")

guess_the_num()

    


