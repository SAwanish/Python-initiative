# It's Time to play-------------with the system------------
import random as rd

rock = '''
    ______
---'   ___)
      (____)
      (____)
      (___)
---.__(__)
'''    
paper = '''
    ______
---'   ___)___
          ____)
          _____)
          ____)
---._________)
'''
scissor = '''
    ______
---'   ___)___
          _____)
        ________)
      (____)
---.__(___)
'''

try:
    count_system = 0
    while True:
        you_chose =int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
        Computer_chose = rd.randint(0,2)
        lst=[rock,paper,scissor]
        print(lst[you_chose])
        print(f"Computer chose:{lst[Computer_chose]}")
        if(you_chose==0 and Computer_chose==1):
            print("You Lose!")
            count_system+=1
        elif(you_chose==1 and Computer_chose==2):
            print("You Lose!")
            count_system+=1
        elif(you_chose==2 and Computer_chose==0):
            print("You Lose!")
            count_system+=1
        elif(you_chose==1 and Computer_chose==0):
            print("You Won")
            print("System Win = {}".format(count_system))
            break
        elif(you_chose==2 and Computer_chose==1):
            print("You Won")
            print("System Win = {}".format(count_system))
            break
        elif(you_chose==0 and Computer_chose==2):
            print("You Won")
            print("System Win = {}".format(count_system))
            break
        else:
            print("Draw, Plz, try again!")
except IndexError:
    print('Wrong input')
