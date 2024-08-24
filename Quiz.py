import turtle
import matplotlib.pyplot as plt


# 1. Create two varables X and y where ? is any number of your choice
# Find x plus y, x divided by y, x minus y , x multipled by y
x = 34
y = 5
print(x + y)
print(x/y)
print(x - y)
print(x*y)

# 2. Create a list of all the even numbers from 0 to 100? Print the first 10 elements and the length of this list
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
# or list1 = list(range(0,101,2)
print(list1[0:10])
print(len(list1))

# 3. Append a value of your choice to the end of this list (is can be any type)?
list1.append(300)
print(list1)

# 4. Assign a variable to any integer you want and using an if statement, find whether this integer is divisable by 5
number = 85
if number % 5 == 0:
    print(" number is divisible by 5")
else:
    print("number is not divisible by 5")

# 5. Using a for loop, get python to print the numbers 0 to 5
for i in range(6):
    print(i)

# 6. Draw a pentagon in turtle?
# turtle.forward(50)
# turtle.left(72)
# turtle.forward(50)
# turtle.left(72)
# turtle.forward(50)
# turtle.left(72)
# turtle.forward(50)
# turtle.left(72)
# turtle.forward(50)
# turtle.left(72)
# turtle.done()
# print(360/5)
# or if i in range(5):
#turtle.left(72)
#turtle.forward(50)


# 7. Create a function that tests whether three numbers (a,b,c) are a Pythagorean triple
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

print(pythagorean_triple(4, 6, 57))
print(pythagorean_triple(3,4,5))


# 8. Create two lists (of size 5 or any size you want) and plot these lists against each other using matplotib?
list3 = [23, 57, 68, 100]
list4 = [43, 48, 59, 87]
plt.plot(list3, list4, c = "blue", linewidth=1, label= "A line", linestyle= "dashed", marker= "s", markerfacecolor="pink", markersize="2")
plt.xlabel("X-axis")
plt.ylabel("Y- axis")
plt.title("Python plot of a line")
plt.legend()
plt.show()



