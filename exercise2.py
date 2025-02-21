import random
counter=0

random_num=random.randint(0,100)
while True:
    guess=int(input("guess a number \n"))
    counter+=1
    if guess > random_num:
        print("guess lower")
    elif guess < random_num:
        print("guess higher")
    else:
        print("YIPEE U GUESSED IT")
        print("It took you a total of "+str(counter)+" guesses.")
        break