import random
user_winning=0
computer_winning=0
symbol=["rock","paper","scissor"]
def computer_game():
    computer_choice=random.choice(symbol).lower()
    return computer_choice
def user_game():
    while(1):
        user_choice=input("enter your choice among 'ROCK'  'PAPER'  'SCISSOR' :").lower()
        if user_choice.isalpha():
            if user_choice == "rock" or user_choice=="paper" or user_choice=="scissor" :
                break
            else:
                print("choose between those three option")
        else:
            print("enter the valid input")
    return user_choice



def game():
    global user_winning
    global computer_winning
    while(1):

        like=input("press enter to play('q' to quit) :").lower()
        if (like=="q"):
            break
        user_choice=user_game()
        computer_choice=computer_game()
        if computer_choice=="rock" and user_choice=="paper":
            print("your choice : PAPER")
            print("computer choice : ROCK")
            print("--you won--")
            user_winning+=1
        elif computer_choice=="rock" and user_choice=="scissor":
            print("your choice : SCISSOR")
            print("computer choice : ROCK")
            print("--computer won--")
            computer_winning+=1
        elif computer_choice=="rock" and user_choice=="rock":
            print("your choice : ROCK")
            print("computer choice : ROCK")
            print("--its a draw--")
        elif computer_choice=="paper" and user_choice=="paper":
            print("your choice : PAPER")
            print("computer choice : PAPER")
            print("--its a draw--")
        elif computer_choice=="paper" and user_choice=="rock":
            print("your choice : ROCK")
            print("computer choice : paper")
            print("--computer won--")
            computer_winning+=1
        elif computer_choice=="paper" and user_choice=="scissor":
            print("your choice : SCISSOR")
            print("computer choice : PAPER")
            print("--you won--")
            user_winning=user_winning+1
        elif computer_choice=="scissor" and user_choice=="scissor":
            print("your choice : SCISSOR")
            print("computer choice : SCISSOR")
            print("--its a draw--")
        elif computer_choice=="scissor" and user_choice=="paper":
            print("your choice : PAPER")
            print("computer choice : SCISSOR")
            print("--computer won--")
            computer_winning+=1
        elif computer_choice=="scissor" and user_choice=="rock":
            print("your choice : ROCK")
            print("computer choice : SCISSOR")
            print("--you won--")
            user_winning=user_winning+1
        print("your wins:",user_winning)
        print("computer wins:",computer_winning)
    return user_winning,computer_winning

game() 