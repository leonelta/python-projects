print("You enter a dark room with two doors. Do you go throughndorr #1 or door #2")

door = raw_input("> ")

if door == "1":
    print("There's a giant bear eating a cheese cake. What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")
    
    bear = raw_input("> ")
    if bear == "1":
        print("Th bear eats your face off. Good job!")
    elif bear == "2":
        print("Th bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bar runs away." % bear)
        
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")
    
    insanity = raw_input(">")
    
    