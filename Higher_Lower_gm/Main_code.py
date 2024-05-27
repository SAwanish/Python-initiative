from game_data import data
from art import logo,vs
from random import randint
from os import system

i=randint(0,49)
j=randint(0,49)
while i==j:
    j=randint(0,49)
game_over=0
current_score=0
# main
while not game_over:
    print(logo)
    print(f"Compare A: {data[i]['name']}, {data[i]['description']}, {data[i]['country']}.")
    A = data[i]['follower_count']
    print(vs)

    print(f"Against B: {data[j]['name']}, {data[j]['description']}, {data[j]['country']}.")
    B = data[j]['follower_count']

    # Compare
    if A>B:
        won='A'
    else:
        won='B'

    who=input("Who has more follwers? Type 'A' or 'B':")
    system('cls')
    if who == won:
        current_score+=1
        print(f"You're right! Current score: {current_score}")
        i=j
        j=randint(0,49)
        while i==j:
            j=randint(0,49)
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        game_over=1