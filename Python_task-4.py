#  Task 1: User Info Manager (Functions + Dictionary)
# Create a function:

def create_user(name,age,role):
    user = {
        "name": name.title(),
        "age" : age,
        "role" : role
    }
    return user


# store User
user = []

# add user
user.append(create_user("Sanjay", 22,"Data analyst"))
user.append(create_user("Arun", 23,"Developer"))
user.append(create_user("Priya", 21,"HR"))

print("All User:\n")
for user in user:
    print(user)



# Task 2: Dynamic Calculator (*args)
# def calculate_total(*numbers):

def calculate_total(*numbers):
    total = sum(numbers)

    if len(numbers)>0:
        averages = total / len(numbers)
    else:
        averages = 0
    return total, averages

result = calculate_total(10,20,20,40)

print("Total:",result[0])
print("averag:", result[1])



# Task 3: Keyword Config System (**kwargs)
# def system_config(**settings):

def system_config(**settings):
    print("System Configuration:\n")

    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode = "debug", version = "1.0", user = "Sanjay")



# Task 4: Factorial Service (Recursion)
# def factorial(n):

def factorial(n):

    if not isinstance(n,int):
        return "Error : Input Must Be Intger"

    if n < 0:
        return "Error : Negative Number Not Allowed"
    
    if n == 0 or n == 1 :
        return 1
    
    return n * factorial (n - 1)

print("factorial of 5 : ", factorial(5))
print("factorial of 0 : " ,factorial(0))
print("factorial of -2: ", factorial(-2))


# Task 5: Memory Optimization (Generator)
# def square_generator(n):

def square_generator(n):
    for i in range(n):
        yield i * i 

gen = square_generator(11)
print("Squares using generator:- ")
for num in gen:
    print(num)


# Normal List
square_list = [i*i for i in range(11)]
print("List: ",square_list)
print("Type: ",type(square_list))


# Generator
square_gen = square_generator(11)
print("Generator: ",square_gen)
print("Type ",type(square_gen))



# Task 6: Exception Handling Module

try:
    numerator = int(input("Enter numerator:- "))
    denominator = int(input("Enter Denominator:- "))

    result = numerator / denominator
    print("Result:- ",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Invalid input (enter numbers only)")
finally:
    print("Program Completed")



# Task 7: File Handling

with open("team_data.txt", "w") as file:
    file.write("Name: sanjay, Role: Data Analyst,\n")
    
    file = open("team_data.txt", "r")
    print("Before closing:", file.closed)

with open("team_data.txt", "r") as file:
    print(file.read())
    
    file.close()
    print("After closing:", file.closed)
