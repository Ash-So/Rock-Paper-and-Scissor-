import random
import time

options=["ROCK","PAPER","SCISSOR"]

comp= random.choice(options)

print("Hello and Welcome to Rock, Paper or Scissor Game!!")
name=input("Enter your name: ").upper()
print("Hey "+name+"!")
time.sleep(1)
print("All the best")
print("Well, let's get started!")
time.sleep(2)

def rps():
    player=input("Please enter either Rock, Paper or Scissor: ")

    if player.upper()==comp:
        print("It's a tie! Try again.")
    elif player.upper()=="ROCK":
        if comp=="PAPER":
            print("You lost. Your opponent chose 'Paper'."
                  "Better luck next time!")
        else:
            print("You WON!. Your opponent chose 'Scissor'.")
    elif player.upper()=="PAPER":
        if comp=="SCISSOR":
            print("You lost. Your opponent chose 'Scissor'."
                  "Better luck next time!")
        else:
            print("You WON!. Your opponent chose 'Rock'.")
    elif player.upper()=="SCISSOR":
        if comp=="ROCK":
            print("You lost. Your opponent chose 'Rock'."
                  "Better luck next time!")
        else:
            print("You WON!. Your opponent chose 'Paper',")
    else:
        print("Please enter a valid option.")

def main():
    rps()
    while input("Play Again? (Y/N) ").upper() == "Y":
        rps()
main()
