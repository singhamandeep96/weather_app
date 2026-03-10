print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

choice=input("Where do you want to go? left or right?")

if (choice=="left"):
    choice2=input("Do you want to wait for a boat or swim?")
    if(choice2=="wait"):
        choice3=input("Which door you want to choose Blue, Yellow Red or anything else ?")
        if (choice3=="Blue"):
            print("Eaten by beasts. Game over")
        elif(choice3=="Red"):
            print("Burned by fire. Game over")
        elif(choice3=="Anything else"):
            print("Game over")
        else:
            print("You win")

    else:
        print("Attacked by trout. Game over.")

else:
    print("Fall into a hole. Game over")