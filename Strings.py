# Strings
# We have already covered strings, integers, floats, booleans and lists
# Integers, floats and booleans are all considered to be simple data types
# They cannot be broken down!

# Lists and strings are different. They are made up of smaller pieces which
# Can be broken down.

# We already know what strings are!
print("Hello world!")
print(type("Hello world!"))

#Operations on strings
# Addition sign concatenation
Greeting = "Hello "
Name = "Maddie"
print(Greeting + Name)

#print("My shoe size is", 7, "and my age is", 21)

# *Operator
print(Greeting*3)
print(Greeting + Name*3)
print(( Greeting + Name )*3)

# Index Operator
Name = "Connie"
print(Name[2]) #the third letter/element of the list
print(Name[0] + Name[3])

# Slicing strings
print(Name[0:4]) # 1st to the 4th letter (0 and 3rd element)
print(Name[2:])

# Lowercase and Uppercase
Name = "maddie"
print(Name.lower())
print(Name.upper())

# Count how many times a character appears in a string
print(Name.count("d"))

# replace specific characters with other characters
print(Name.replace("d", "f"))
Name = "Maddie"
New_Name = Name.replace("d", "f")
print(New_Name)

#Finding the length of the string
print(len(Name))

#Format strings
# your_name = input("Your name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Each letter in python is assigned to a specific number!
print("orange" < "strawberry") # True
print(ord("o")) #111
print(chr(38)) # &
# We can perform maths on strings!

# in and no operators
fruit = "banana"
print("a" in fruit) # print whether a is in fruit
print("s" not in fruit)

# Incorporate a few things we've learnt so far
x = "hello"
y = ""
for character in x:
    y = character.upper() + y
print(y)




