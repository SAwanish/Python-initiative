# Blind Auction Program
from os import system
from art import logo
print(logo)
Bidders={}
Is_anyone_else_to_bid="yes"
while Is_anyone_else_to_bid=="yes":
    name=input("What is your name? :")
    bid=int(input("What's your bid? : $"))
    Bidders[name]=bid
    Is_anyone_else_to_bid=input("Are there other bidders? Type 'yes' or 'no'.")
    system('cls')
max=0
naam="no_one"
for person in Bidders:
    if Bidders[person]>max:
        max=Bidders[person]
        naam=person
print(f"The winner is {naam} with a bid of ${max}.")