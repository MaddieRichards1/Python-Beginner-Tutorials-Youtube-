import random

# p = random.randrange(-10, 23) #randrange goes up to but doesn't include the final number
# r = random.randint(3, 24) # randint does include the last number
# print(r)

top_of_range = input("Type a number ")

if top_of_range.isdigit(): #is it a number then  #make sure input string is converted to a number
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 nex time")

else:
    print("Please type a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():  # is it a number then  #make sure input string is converted to a number
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    else: #or use elif
        if user_guess > random_number:
            print("You were above the number")
        else:
            print("You were below the number")



print("You got it in", guesses, "guesses")
