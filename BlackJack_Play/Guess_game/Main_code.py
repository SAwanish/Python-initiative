# Guessing Game
import random as rd
from os import system
from art import logo
def guess_game():
    system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")

    num=rd.randint(1,100)

    if difficulty=='easy':
        print("You have 10 attempts remaining to guess the number.")
        for i in range(10):
            guess=int(input("Make a guess:"))
            if guess>num:
                print("Too high.\nGuess again.")
                print(f"You have {9-i} attempts remaining to guess the number.")
            elif guess<num:
                print("Too low.\nGuess again.")
                print(f"You have {9-i} attempts remaining to guess the number.")
            else:
                print(f"You guessed the correct number:{guess}, Congrats!!")
                break

    elif difficulty=='hard':
        print("You have 5 attempts remaining to guess the number.")
        for i in range(5):
            guess=int(input("Make a guess:"))
            if guess>num:
                print("Too high.\nGuess again.")
                print(f"You have {4-i} attempts remaining to guess the number.")
            elif guess<num:
                print("Too low.\nGuess again.")
                print(f"You have {4-i} attempts remaining to guess the number.")
            else:
                print(f"You guessed the correct number:{guess}, Congrats!!")
                break

    else:
        what=input("Invalid Input!!")
guess_game()