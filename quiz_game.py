print("Welcome to my geography quiz")

playing = input("Do you want to play? ") # make sure to add space after

if playing.lower() != "yes":  # does not is !=
    quit()
print("Okay! Let's play!!")
score = 0

answer = input("What is the capital of UK? ")
if answer.lower() == "london":
    print("Correct")
    score +=1 #score + 1
else:
    print("Incorrect!")

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Germany? ")
if answer.lower() == "berlin":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Norway? ")
if answer.lower() == "oslo":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
#str(score) because it is a integer
print("You got " + str((score / 4) *100) + "%")
