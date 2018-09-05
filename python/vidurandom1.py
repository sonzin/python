import random
choiceNumber = random.randrange(0, 3)  # to get a 0, 1, or 2
if choiceNumber == 0:
    randomChoice = 'rock'
elif choiceNumber  == 1:
    randomChoice = 'paper'
else:  # not zero and not one, must be 2
    randomChoice == 'scissors'
print(randomChoice)
