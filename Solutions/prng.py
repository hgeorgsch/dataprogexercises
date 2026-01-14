# From Mateusz
# My proposal for the solution of "Litt større oppgåva" from "tilfeldig tall generator" :
#
# I tried to use what should already be known to the students at this stage of the course, and I think they will rather not have much problems with the task. It is well documented and explained.





import random

red = [ 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3 ]
black = [ 15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26 ]

def win(number, bet):
    if bet == 'red':
        return number in red # returns true or false,
    elif bet == 'black':
        return number in black
    else:
        return False

def spin():
    return random.randint(0,36)

def factorValue(lst):
    return 36/len(lst)

def payoff(number, bet, stake):
    if win(number, bet):
        if bet == 'red':
            factor = factorValue(red)
            return stake * factor
        elif bet == 'black':
            factor = factorValue(black)
            return stake * factor
    return 0

def play(bet, stake):
    number = spin()
    return payoff(number, bet, stake)
"""
rounds = 1000
stake = 1
total = 0

for _ in range(rounds):
    total += play('red',stake) - stake
print(total)
"""

runs = 5
run = 0
rounds = 1000
stake = 1
results = []

while run < runs:
    total = 0
    run += 1
    for _ in range(rounds):
        total += play('red',stake) - stake
    results.append(total)

average = sum(results)/len(results)

print(f"res: {results}, avg: {average:.2f}")

