import random
import time

def generate_wheel():
    spaces=[]
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spin_wheel(spaces):
    return random.choice(spaces)

def play_game():
    spaces=generate_wheel()
    print(spaces)
    money=1000
    while True:
        print("you have $"+str(money))
        bet=int(input("how much do want to bet?"))
        while bet>money:
            bet=int(input("YOU HAVE LESS THAN THAT MUCH MONEY!! PUT LESS"))
        color=input("what color do you want to bet on?")
        print("The wheel is spining.......")
        time.sleep(2)
        landed=spin_wheel(spaces)
        print("It landed on "+landed)
        if color==landed:
            money=money+bet
            print("congrats! you now have $"+str(money))
        else:
            money=money-bet
            print("Womp Womp! you now have $"+str(money))
        if money<=0:
            print("GET OUT")
            break
        play_again=input("wanna play again?")
        if play_again=="no":
            break
play_game()