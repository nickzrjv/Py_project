print("Welcome to Rock,Paper,Scissors!!")

a=input("Make your choice;rock, paper or scissors? : ").lower()   #user_choice is a
import random

choices=["rock", "paper", "scissors"]
b= random.choice(choices)  #computer_choice is b


while a not in ["rock", "paper", "scissors"]:
    print("Invalid choice.Please try again")
    a=input("Make your choice;rock, paper or scissors? : ").lower()
    print(a)

if a=="paper" and b=="rock":
    print("Yay!You won; Computer choice is",b)
elif a=="rock" and b=="scissors":
    print("Yay!You won; Computer choice is",b)
elif a=="scissors" and b=="paper":
    print("Yay!You won; Computer choice is",b)
elif a==b:
    print("It's a tie; Computer choice is also",b)
else:
    print("Oops!You lost :( ; Computer choice is",b)
