print("Hello, This is my final project")
name = (input("What is your name? "))
print("Hi " + name + ", nice to meet you")

print("This is a special calculator, I would need two numbers from you")
number_1 = int(input("First number "))
number_2 = int(input("Second number "))
print("Thank you for putting in your numbers, " + str(number_1) + " and " + str(number_2))

even_number_1 = number_1 % 2 == 0
even_number_2 = number_2 % 2 == 0

if even_number_1:
    even_number_1 = "even"
else:
    even_number_1 = "odd"

if even_number_2:
    even_number_2 = "even"
else:
    even_number_2 = "odd"

print("I can see that the first number is " + even_number_1)
print("And the second is " + even_number_2)

if even_number_1 == even_number_2 == "even":
    print("So both of them are even")
elif even_number_1 == even_number_2 == "odd":
    print("So both are odd")
else:
    print("So one of them is even, and one is odd")

# I used those orders before but "else" didn't work well:
# if even_number_1 and even_number_2 == "even":
#     print("So both of them are even")
# elif even_number_1 and even_number_2 == "odd":
#     print("So both are odd")
# else:
#     print("So one of them is even, and one is odd")

operator = input("Operator (+, -, *, /): ")

add = number_1 + number_2
sub = number_1 - number_2
multi = number_1 * number_2

total = ""

# In this case I had to duplicate the line: print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(total))

if operator == "+":
    total = add
    print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(total))
elif operator == "-":
    total = sub
    print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(total))
elif operator == "*":
    total = multi
    print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(total))
elif operator == "/":
    division = input("You chose division, should the result be integer? (y/n) ")
    if number_2 == 0:
        print("Error: num_2 is zero")
        print("An error had occured, please try again")
    elif division == "y":    
        total = number_1 // number_2
        print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(total))
    else:
        total = number_1 / number_2
        print(str(number_1) + " " + operator + " " + str(number_2) + " = " + str(total))
else:
    print("Error: Operator " + operator + " is not supported")
    print("An error had occured, please try again")

import time
print("Thank you " + name + " for using the calculator on " + time.ctime())