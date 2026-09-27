import random

def guess(x):
    n=random.randint(1,x)
    
    i=1
    while(1):
        m=int(input("enter the number in range 0-100:"))
        if n>m:
            print("enter the bigger number")
        elif n<m:
            print("enter the smaller number")
        elif n==m:
            print("congrats you guesssed corrrect")
            break
        else:
            print("invalid input")
        i=i+1
    print(f" the number computer choosen is :{n}")
    print("the number of gueses u made is :",i)

guess(100)





