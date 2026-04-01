# Task 1: Encapsulation (User Class)
#  Create a class User with proper encapsulation.


class User:
    def __init__(self):
        self.__user_name = None   
        self.__pwd = None         
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd
    def get_user(self):
        return self.__user_name
    def register(self):
        print(f"Registering user: {self.__user_name}")
    def login(self):
        print(f"Logging in: {self.__user_name}")


user1 = User()
user1.set_user("john", "1234")

user1.register()
user1.login()



# Task 2: Inheritance (User → Student, Faculty)
# Create parent class User


class User:
    def register(self):
        print("User registered")

    def login(self):
        print("User logged in")
        
class Student(User):
    def student_greet(self):
        print("Hello Student")
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")

s1 = Student()
s1.register()        
s1.login()          
s1.student_greet()   

print("-----")
f1 = Faculty()
f1.register()    
f1.login()           
f1.faculty_greet()   

print("-----")

t1 = TempFaculty()
t1.register()              
t1.login()                 
t1.faculty_greet()         
t1.tempFaculty_greet() 



# Task 3: Method Overriding
# Use same User, Student, Faculty


class User:
    def greet(self):
        print("Welcome User")
class Student(User):
    def greet(self):
        print("Welcome Student")
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")

student = Student()
faculty = Faculty()

student.greet()
faculty.greet()



# Task 4: Method Chaining
# Create class User


class User:
    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

user = User()

user.login().greet().register()



# Task 5: Combined Task (Real-Time)
# Build a Mini User System

class User:
    users_count = 0
    def __init__(self, name, password):
        
        self.__name = name
        self.__password = password
        User.users_count += 1
    def get_name(self):
        return self.__name
    def register(self):
        print("registered")
        return self
    def login(self):
        print("logined")
        return self
    def greet(self):
        print("Welcome User")
        return self
class Student(User):
    def greet(self):
        print("Welcome Student")
        return self
class Faculty(User):
    def greet(self):
        print("Welcome Faculty")
        return self
s1 = Student("john", "1234")
f1 = Faculty("alice", "5678")
s1.login().greet().register()
print("-----")
f1.login().greet().register()
print("-----")
print("Total users:", User.users_count)
