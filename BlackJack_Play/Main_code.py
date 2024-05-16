import random as rd
from os import system
from Logo import logo
def blackjack():
    system('cls')
    print(logo)
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    your_cards=[]
    computer_cards=[]

    for i in range(2):
        your_cards.append(cards[rd.randint(0,12)])
        computer_cards.append(cards[rd.randint(0,12)])
    print(f"Your cards: {your_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    add_card=input("Type 'y' to get another card, type 'n' to pass: ")

    while add_card=='y':
        your_cards.append(cards[rd.randint(0,12)])
        if (your_cards[0]==11 or your_cards[1]==11 or your_cards[2]==11)and sum(your_cards)>21:
                index=your_cards.index(11)
                your_cards[index]==1
        if sum(your_cards)>21:
            print(f"Your final hand: {your_cards}\nComputer's final hand:{computer_cards} \nYou went over. You lose 😭")
            print(f"Your final score: {sum(your_cards)}")
            print(f"Computer's final score: {sum(computer_cards)}")
            exit()
        else:
            print(f"Your cards: {your_cards}")
            print(f"Computer's first card: {computer_cards[0]}")
            add_card=input("Type 'y' to get another card, type 'n' to pass: ")
        
    if add_card=='n':
        if sum(computer_cards)<=16 and sum(computer_cards)<=sum(your_cards):
            computer_cards.append(cards[rd.randint(0,12)])           

        if sum(your_cards)>21:
            if your_cards[0]==11 or your_cards[1]==11 or your_cards[2]==11:
                index=your_cards.index(11)
                your_cards[index]==1
            else:    
                print(f"Your final hand: {your_cards}\nComputer's final hand:{computer_cards} \nYou went over. You lose 😭")
        elif sum(computer_cards)>21:
            if your_cards[0]==11 or your_cards[1]==11 or your_cards[2]==11:
                index=your_cards.index(11)
                your_cards[index]==1
            print(f"Your final hand: {your_cards}\nComputer's final hand:{computer_cards} \nComputer went over. You Won 😄")
        elif sum(your_cards)> sum(computer_cards):
            print(f"Your final hand: {your_cards}\nComputer's final hand:{computer_cards} \nYou Got it. You Won 😄")
        elif sum(your_cards)==sum(computer_cards):
            print(f"Your final hand: {your_cards}\nComputer's final hand:{computer_cards} \nBoth got same score. You made it Draw 😀")
        else:
            print(f"Your final hand: {your_cards}\nComputer's final hand:{computer_cards} \nYou went over. You lose 😭")

        print(f"Your final score: {sum(your_cards)}")
        print(f"Computer's final score: {sum(computer_cards)}")
        print("😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀\n😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀")
        play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if play=='y':
            blackjack()
        
            
play=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if play=='y':
    blackjack()
else:
    print("Not a Problem!!")