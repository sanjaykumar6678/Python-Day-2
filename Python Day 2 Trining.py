# Bitwise Operator Tasks

# 1.Create two variables a = 10 and b = 6.(AND)
a = 10 
b = 6
print (a&b)

# 2.Create two variables x = 12 and y = 5.(OR)
x = 12
y = 5
print(x|y)

# 3.Create a variable num = 8.(NOT)
num = 8
print(~num)

# 4. Create two variables a = 15 and b = 9.
a = 15
b = 9
print(a^b)

# 5.Create a variable num = 7.(Left Shift)
num = 7
result = num << 2
print(result)

# 6.Create a variable num = 20.(Right Shift)
num1 = 20
result1 = num >> 1
print(result1)

# 7.Take two numbers from user input and print AND result.

marks = int(input("Enter Your mark:- "))
age = int(input("Enter Your age:- "))
print("AND result:", marks & age)

# 8.Take two numbers from user input and print XOR result.

num1 = int(input("Enter your Roll Number:- "))
num2 = int(input("Enter Your Batch Number:- "))
result = num1 ^ num2
print("XOR result: ", result)


# String Tasks

# 9.Create a string "hi" and print it 4 times using replication.
text1='hi'
print(text1*4)

# 10.Create a string "python" and print it 3 times.
text2= "Python"
print(text2*3)

# 11.Create two strings "super" and "man" and combine them using + operator.
a = "super"
b = "man"
print(a+b)

# 12.Create three strings "hello", " ", "world" and print "hello world".

a = "hello"
b = " "
c = "world"
print(a+b+c)

# 13.Take a name from user input and print it 5 times.
name =input("Enter your name:- ")
print(name*5)

# 14.Take two strings from user input and concatenate them.

str1 =input("Enter your first name:- ")
str2 =input("Enter your last name:- ")
print(str1 + str2)


# Input & Type Casting Tasks

# 15. Take a name from user input and print its data type.

name =input("Enter your name:- ")
print(type(name))

# 16. Take age from user input and convert it into integer.

age = int(input("Enter Your Age:- "))
print(type(age))

# 17.Take two numbers from user input and print their sum.

num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))
print("Sum :", num1 + num2)

# 18.Take two marks from user input and print their average.

marks1 =int(input("Enter first mark:- "))
marks2 =int(input("Enter second mark:- "))
average = (marks1 + marks2)/2
print("Average:",average)

# 19. Take two numbers from user input and print

a = int(input("Enter value of a: ")) #3
b = int(input("Enter value of b: ")) #2
print(3*a*2 + b - 2)

# 20. Take a number from user input and print its data type before and after type casting.

num = input("Enter a number:- ")
print("Before type casting:- ", type(num))
num =int(num)
print("After type casting:- ",type(num))


# Unit Digit Tasks

# 21. Take a number as string input and print the last digit.

num =input("Enter a number:- ")
print("Last digit", num[-1])

# 22. Take a number and print the unit digit using % operator.

num = int(input("Enter a number:- "))
print("Unit digit",num % 10)

# 23. Take a number and remove the last digit using // operator.

num = int(input("Enter a number:- "))
print("Removing Last digit; ", num//10)

# 24. Take a number and print the second last digit.

num = int(input("Enter a number:- "))
second_last = (num // 10) % 10
print("Second Last Digit: ",second_last)

# 25. Take a 5 digit number and print its last digit.

num = int(input("Enter a 5 digit number:- "))
print("Last digit: ",num % 10)


# If Statement Tasks 

# 26. Create a program that checks if 10 ≥ 5 and prints a message.

if 10 >= 5:
    print("10 is greater than or equal to 5")


# 27. Take a number from user input and check if it is greater than 50.

num = int(input("Enter a number:- "))
if num > 50:
    print("Number is greater than 50")

# 28. Take age from user input and check if age ≥ 18.

age = int(input(" Enter Your Age:- "))
if age >= 18 :
    print("Your Are Eligible")

# 29. Take a number and check if it is greater than 100.

num = int(input("Enter a number:- "))
if num > 100 :
    print("Number is greater Than 100")


# 30. Take a number and check if number ≥ 0.
num = int(input("Enter a number:- "))
if num >=0 :
    print("Number is positive")



# If-Else Tasks 

# 31. Take a number and check if it is even or odd.
 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

# 32. Take marks from user input and check if pass or fail (pass ≥ 35).

marks = int(input("Enter Marks:- "))
if marks >=35:
    print("Pass")
else:
    print("Fail")

# 33. Take a number and check if it is positive or negative.

num = int(input("Enter a number:- "))
if num >0:
    print("Positive")
else:
    print("Negative")

# 34. Take a number and check if it is greater than 10 or not.

num = int(input("Enter a number:- "))
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than")


# Nested If Tasks

# 35. Create a program for job eligibility:
# Age ≥ 18
# Height ≥ 160
# Weight ≥ 60

age = int(input("Enter your age:- "))
height = int(input("enter your height:- "))
weight = int(input("Enter your weight:- "))
if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected") 


# 36. Create a college admission program:
#Marks ≥ 60
#Age ≥ 17

marks = int(input("Enter Marks:- "))
age = int(input("Enter age:- "))
if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")       


# 37. Create a sports selection program:
#Age ≥ 16
#Height ≥ 150
#Weight ≥ 50

age =int(input("Enter your age:- "))
height = int(input("Enter your height:- "))
weight = int(input("Enter your weight:- "))
if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Congratulations Your Are selected")
        else:
            print("Not Selected")
    else:
        print("Not Selected")
else:
    print("Not Selected")



# Match Statement Tasks

# 38. Take a number (1-7) and print day name using match.

day =int(input("Enter Number (1-7):- "))

match day :
    case 1 :
        print("Sunday")
    case 2 :
        print("Monday")
    case 3 :
        print("Tuesday")
    case 4 :
        print("Wednesday")
    case 5 :
        print("Thursday")
    case 6 :
        print("Friday")
    case 7 :
        print("Saturday")                


# 39. Take a number (1-3) and print:
#1 → Red
#2 → Blue
#3 → Green

color = int(input("Enter Your Number:- "))

match color:
    case 1 :
        print("Red")
    case 2 :
        print("Blue")
    case 3 :
        print("Green")


# 40. Take a number (1-4) and print:
#1 → Apple
#2 → Mango
#3 → Orange
#4 → Banana

fruit = int(input("Enter a number:- "))

match fruit :
    case 1 :
        print("Apple")
    case 2 :
        print("Mango")
    case 3 :
        print("Orange")
    case 4 :
        print("Banana")
    
