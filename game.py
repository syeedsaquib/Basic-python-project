import random
target = random.randint(1,100)

while True:
    n = int(input("Enter your guesses number(between 1 - 100) or Quit(-1) :- "))

    if(n == -1):
        break
    elif(n == target):
        print("Your guess is right....!")
        break
    elif(n > target):
        print("Number is too big")
    else:
        print("Number is too small")


print(".......Game Over.........")