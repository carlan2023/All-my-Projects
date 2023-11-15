import random
def guess(x):
    random_number =random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input (f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print ('Ooops too low')
        elif guess > random_number:
            print ('Hihi too high')
            
    print("You have started thinking like the gods. The number is " + str(random_number))
guess(10)
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback !='c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback = input(f'Is {guess} lower[l], higher[h] or correct[c]')
        if feedback == 'l':
            low =guess+1
        elif feedback == 'h':
            high = guess-1
    print(f'I have started thinking like people. The number is, {guess}, thanks')
computer_guess(10000)
    
