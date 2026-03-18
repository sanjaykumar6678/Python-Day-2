# Section 1: Loop Basics

# 1. Print numbers from 1 to 50 using for loop

for i in range(1,51):
    print(i)


# 2.Print even numbers from 1 to 100

for i in range(2,101,2):
    print(i)

# 3. Print odd numbers from 1 to 100

for i in range(1,101,2):
    print(i)


# 4. Print multiplication table of 7

for i in range(1,11):
    print(f"7 x {i} = {7*i}")


# 5. Find sum of numbers from 1 to 100

total = 0
for i in range(1,101):
    total += i
print("Sum =",total)


# 6. Print numbers in reverse from 50 to 1

for i in range(50,0,-1):
    print(i)


# 7. Count how many numbers are divisible by 3 (1–100)

count = 0
for i in range (1,101):
    if i % 3 == 0:
        count += 1
print("Count:-",count)


# 8. Print squares of numbers from 1 to 10
for i in range(1,11):
    print(i, "Square:- ",i*i)

# 9.Print cube of first 10 numbers

for i in range (1,11):
    print(i,"Cube:- ",i**3)


# 10. Take input n, print numbers from 1 to n

n = int(input("Enter number:- "))
for i in range(1,1+n):
    print(i)



# Section 2: While Loop

# 11.Print numbers from 1 to 20 using while

i = 1
while i <= 20:
    print(i)
    i += 1

# 12. ind factorial of a number using while

n = int(input("Enter Number:- "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:- ", fact)

# 13 . Reverse a number using while

n = int(input("Enter Number:- "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed:- ", rev)

# 14 . Count digits in a number

n = int(input("Enter Number:- "))
count = 0
while n > 0:
    count += 1
    n = n // 10
print("Digits = ",count)

# 15 . Keep asking input until user enters "stop"

while True :
    text = input ("Enter name:- ")
    if text == "stop":
        break



# Section 3: Nested Loop

# 16 . Print pattern:

for i in range(1, 5):
    for j in range (i):
        print("*", end=" ")
    print()

# 17 . Print pattern:

for i in range(1,5):
    for j in range (1,i+1):
        print(j, end="")
    print()    


# 18 . Print multiplication table (1 to 5) using nested loop

for i in range(1,6):
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}" )
    print()


# 19 . Print patten (ABC)

for i in range(3):
    for j in range(3):
        print(chr(65 + j), end = " ")
    print()


# 20 . Print Number Patten (123)

num = 1
for i in range (3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()



# Section 4: String Basics

# 21 . Count total characters in a string

text = input("Enter String:- ")
count = 0
for ch in text:
    count += 1
print("Total Character:- ", count)

# 22. Count vowels in a string

text = input("Enter Letter:- ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Vowels:-", count)

# 23. Count consonants in a string

text = input("Enter Number:- ")
count = 0

for ch in text.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("Consonants:- ", count)


# 24. Reverse a string using loop

text = input("Enter Value:- ")
rev = ""

for ch in text:
    rev = ch + rev
print("Reverse Value:- ", rev)


# 25 . Check if string is palindrome

text = input("Enter Values:- ")
rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("palindrome")
else:
    print("Not palindrome")
  


# Section 5: String Slicing

# 26 . Print first 5 characters of a string

text = input("Enter Your Name:- ")
print(text[:5])

# 27 . Print last 3 characters

text = input("Enter youe name:- ")
print(text[-3:])

# 28 . Print string in reverse using slicing

text = input("Enter values:- ")
print(text[::-1])

# 29 . Print every 2nd character

text = input("Enter Letter:- ")
print(text[::2])

# 30. Remove first and last character from string

text = input("Enter Your name:- ")
print(text[1:-1])

# Section 6: List Basics


# 31. Create a list of 5 numbers and print sum

nums = [1,2,3,4,5]
print("Sum =",sum(nums))

# 32. Find maximum value in list

nums = [10,20,30,40,50]
print("Max =",max(nums))

# 33 . Find minimum value in list

nums = [10,25,5,40]
print("Min =",min(nums))

# 34. Count total elements in list

nums = [1,3,4,6,6]
count = 0

for i in nums:
    count += 1
print("Total Elements:- ",count)

# 35 . Check if element exists in list

nums = [10,20,30,40,50]

value = int(input("Enter number:- "))

if value in nums:
    print("Exists")
else:
    print("Not Exists")


# Section 7: List Operations
 
# 36 . Add 3 elements using append()

num = []
num.append(10)
num.append(20)
num.append(30)

print(num)

# 37. Insert element at specific index

num = [1,3,5,7]
num.insert(4,9)

print(num)

# 38 . Remove element using remove()

nums = [10,20,30,40]
nums.remove(30)

print(nums)

# 39 . Reverse list without using .reverse()

nums = [1,2,3,4,5]

rev = []

for i in range(len(nums)-1,-1,-1):
    rev.append(nums[i])
print(rev)

# 40 . Sort list without using .sort()

nums = [5,2,7,8,1]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)