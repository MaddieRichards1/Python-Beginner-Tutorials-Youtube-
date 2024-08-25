name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You come to a cross roads do you turn left or right? ").lower()
if answer  == "left":
    answer = input("You come to a river one the wooden bridge leads to a pack of wolves the metal bridge leads to the poison ivy. Do you choose the wooden or metal bridge? ")

    if answer == "wooden":
        answer = input("Do you decide to fight the wolves with a sword or bow and arrow? ")
        if answer == "sword":
            print("Well done you have survived!")

        elif answer == "bow and arrow":
            print("Too slow you were killed by wolves")

        else:print("Not a valid option. You lose.")


    elif answer == "metal":
        answer = input("You got stung by poison ivy. Do you find herbs to cure it or leave it alone?")
        if answer == "find herbs":
            print("well done you have survived")
        elif answer == "leave it alone":
            print("Silly choice you have poisoned yourself")
        else: print("Not a valid option. You lose.")

    else: print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("bandits attack you and try and steal your money. Do you let them or fight back? ")

    if answer == "let them":
        print("Coward you lost all your money and were left in a ditch")
    elif answer == "fight back":
        answer = input("They go off running and you steel all their money. What do you do with the money go to the pub or buy a horse? ")
        if answer == "go to the pub":
            print("Idiot! You lost all your money gambling")
        elif answer == "buy a horse":
            print("Well done! You actually make it to your destination quicker with nothing stopping you")
        else:print("Not a valid option. You lose.")

    else:print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

