import random
colour = random.choice(["red", "blue", "green", "white", "pink"])
tryagain = true
while tryagain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()
    if colour == theirchoice:
        print("Well done")
        tryagain = False
    else:
        if colour == "red":
            print("I bet you are seeing Red right now!")
        elif colour == "blue":
            print("Don't feel BLUE")
        elif colour == "green":
            print("I bet you are GREEN with envy right now.")
        elif colour == "white":
            print("Are you WHITE a sheet, as you didn't guess correctly?")
        elif colour == "pink":
            print("Shame you are not feeling in the Pink, as you got it wrong!")
            
    