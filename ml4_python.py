'''python code for hungman game'''
import random

ANS_LIST = ["apple", "banana", "grapes", "watermelon", "strawberry"]
random.shuffle(ANS_LIST)
ANSWER = list(ANS_LIST[0])

DISP = []
USED = []
DISP.extend(ANSWER)
USED.extend(DISP)

for i in range(len(DISP)):
    DISP[i] = "_"

print(' '.join(DISP))
print()
COUNT = 0

while COUNT < len(ANSWER):
    GUESS = input("Please guess the name of fruit: ")
    GUESS = GUESS.lower()
    print(COUNT)

    for i in range(len(ANSWER)):
        if ANSWER[i] == GUESS and GUESS in USED:
            DISP[i] = GUESS
            COUNT = COUNT + 1
            USED.remove(GUESS)


    if GUESS not in DISP:
        print("sorry,wrong guess")



    print("You have guessed: ", COUNT, "correct letters.")
    print(' '.join(DISP))
    print()

print("well done, you guessed the fruit")
