import random

Ans_LIST = ["apple", "banana", "grapes", "watermelon", "strawberry"]
random.shuffle(Ans_LIST)
Answer = list(Ans_LIST[0])

Disp = []
USED = []
Disp.extend(Answer)
USED.extend(Disp)

for i in range(len(Disp)):
    Disp[i] = "_"

print(' '.join(Disp))
print()
Count = 0

while Count < len(Answer):
    GUESS = input("Please guess the name of fruit: ")
    GUESS = GUESS.lower()
    print(Count)

    for i in range(len(Answer)):
        if ANSWER[i] == GUESS and GUESS in USED:
            Disp[i] = GUESS
            Count = Count + 1
            USED.remove(GUESS)


    if GUESS not in Disp:
        print("sorry,wrong guess")



    print("You have guessed: ", COUNT, "correct letters.")
    print(' '.join(Disp))
    print()

print("well done, you guessed the fruit")
