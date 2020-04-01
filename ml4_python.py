import random

ANS_LIST = ["apple", "banana", "grapes", "watermelon", "strawberry"]
random.shuffle(ANS_LIST)
Answer = list(ANS_LIST[0])

DISP = []
USED = []
DISP.extend(Answer)
USED.extend(DISP)

for i in range(len(DISP)):
    Disp[i] = "_"

print(' '.join(DISP))
print()
Count = 0

while Count < len(Answer):
    GUESS = input("Please guess the name of fruit: ")
    GUESS = GUESS.lower()
    print(Count)

    for i in range(len(Answer)):
        if Answer[i] == GUESS and GUESS in USED:
            DISP[i] = GUESS
            Count = Count + 1
            USED.remove(GUESS)


    if GUESS not in DISP:
        print("sorry,wrong guess")



    print("You have guessed: ", COUNT, "correct letters.")
    print(' '.join(DISP))
    print()

print("well done, you guessed the fruit")
