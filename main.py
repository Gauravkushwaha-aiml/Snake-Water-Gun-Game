import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

youDict = {
    "s": 1,
    "w": -1,
    "g": 0
}

reverseDict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

you = youDict[youstr]

print("You chose", reverseDict[you])
print("Computer chose", reverseDict[computer])

if computer == you:
    print("It's a Draw!")
elif computer == -1 and you == 1:
    print("You Win!")
elif computer == -1 and you == 0:
    print("You Lose!")
elif computer == 1 and you == -1:
    print("You Lose!")
elif computer == 1 and you == 0:
    print("You Win!")
elif computer == 0 and you == -1:
    print("You Win!")
elif computer == 0 and you == 1:
    print("You Lose!")