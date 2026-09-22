import random
max_lines=3
max_bet=100
min_bet=1

rows=3
cols=3
symbols={"A":2,"B":4,"C":6,"D":8}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_win(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if  symbol != symbol_to_check:
                break
        else:
            winnings+= values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines
def deposit():
    
    while(1):
        amount=input("enter how much money you like to deposit:")
        if(amount.isdigit()):
            amount=int(amount)
            if amount>0:
                break   #used to exit loop 
            else:
                print("amount must be greater than 0")

        else:
            print("please enter the valid amount")  
    return amount  # fun going to return me amount   
def get_number_of_lines():
    while(1):
            lines=input("enter no of lines you like to bet on (1-"+ str(max_lines) + ")?")
            if(lines.isdigit()):
                lines=int(lines)
                if 1<=lines<=max_lines:
                    break   #used to exit loop 
                else:
                    print("enter valid no of lines")
    
            else:
                print("please enter the number ")  
    return lines 

def place_bet():
      #so problem here is how can i get the variable lines and balance in this function
    while(1):
        bet_amount=input("enter the amount to bet on each line ? :")
            
        if(bet_amount.isdigit()):
            bet_amount=int(bet_amount)
                
            if min_bet<=bet_amount<=max_bet:
                break   #used to exit loop 
            else:
                print(f"amount must be b/w {min_bet} and {max_bet}")
        
        else:
            print("please enter the number ")  
    return bet_amount 

def slot_machine(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):  # we are going to add the 3 column in the list columns .
        new_symbols=all_symbols[:] 
        column=[]         #each column contain the diff syb randomly choosen by computer
        for _ in range(rows):
            
            value=random.choice(new_symbols)
            column.append(value)
            new_symbols.remove(value)
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def spin(balance):
    lines=get_number_of_lines()
        
    while(1):
        bet_amount=place_bet()
        total_bet=bet_amount*lines
        if (total_bet> balance):
            print("you do not have enough balance")
            print("your balance :",balance)
        else:
            break
    print(f"Total bet placed is :",total_bet)
    slots=slot_machine(rows,cols,symbols)
    print_slot(slots)
    winnings,winning_lines=check_win(slots,lines,bet_amount,symbol_value)
    print(f"you won ${winnings}.")
    print(f"you won on",*winning_lines)
    return winnings - total_bet

def main():
    balance=deposit()  # diff b/w global and local variable
    while True:
        print(f"current balance is ${balance}")
        answer=input("press enter to play (q to quit). ")
        if answer=="q":
            break
        balance += spin(balance)
    print(f"you left with ${balance}")

main()