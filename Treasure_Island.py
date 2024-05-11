# Treasure Island ---- Ready to play---------
print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")
side=input("You're at a cross road. Where do you wanna go? Type "'left'" 'or' "'right'" ")
if(side=="right"):
    print("Game Over.")
else:
    lake=input("You came to lake. There is an island in the middle of the lake. Type "'wait'" to wait for a boat. Type "'swim'" to swim across.")
    if(lake=="swim"):
        print("Game Over.")
    else:
        island=input("YOu arrive at the unharmed . There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if(island=="yellow"):
            print("You Win!")
        else:
            print("Game Over.")