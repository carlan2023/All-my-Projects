import random
def play():
    user = input("'r' fro rock, 'p' for paper and 's' for scissors\n")
    computer =random.choice(['r','p','s'])
    if user == computer:
        return'Its a tie'
    if win(user,computer):
        return 'You win'
    return 'You lost'
#r>p,p>s, s>r
def win(player, opponent):
    if(player=='r' and opponent =='p') or (player=='p' and opponent=='s') or (player=='s' and opponent=='r'):
        return True
    
while True:
    print (play())
    

    
