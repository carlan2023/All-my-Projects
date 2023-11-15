import random
MAX_LINES=3
MAX_BET =100
MIN_BET=1

ROWS=3
COLS =3
symbol_count = {
    "A":2
    "B":4
    "C":6
    "D":8
    }
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Amount should be in Integers")
    return(amount)

def get_number_of_lines():
    while True:
        lines = input("How many lines do you want to bet on? ( 1 -" +str(MAX_LINES)+"")
        if lines.isdigit():
            lines=int(lines)
            if 1 <=lines<=MAX_LINES:
                break
            else:
                print("lines must be greater than zero")
        else:
            print("lines should be in Integers") 
    return(lines)

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must between ${MIN_BET}-${MAX_BET} ")
        else:
            print("Amount should be in Integers")
    return(amount)
    
    
def main():
    balance= deposit()
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print('You cannot bet more than $ ',balance)
        if total_bet > MAX_BET:
            print(f"Your bet cannot be greater than {MAX_BET} ")
        else:
            break
    print(f"You are betting {bet} on {lines} lines a total bet of {total_bet} $ ")
    
main()
    

