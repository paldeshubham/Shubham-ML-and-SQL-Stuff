# class User:
#     def __init__(self):
#         self.name = 'Nitish'
#         self.gender = 'male'
    
#     def login(self):
#         print('login')

# class Student(User):
#     def __init__(self):
#         super().__init__()  # Calls User's __init__, so name & gender are initialized
#         self.rollno = 100  

#     def enroll(self):
#         print('enroll into the course')

# u= User()
# s = Student()
# print(s.name)  # ✅ Works fine, prints "Nitish"
# print(s.gender)  # ✅ Works fine, prints "male"
# print(s.rollno)  # ✅ Works fine, prints 100



# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print ("Buying a phone")
# class SmartPhone(Phone):
#     pass


# s=SmartPhone(20000, "Apple", 13)
# s.buy()


#child  cant access the private members of the class


# class Phone:

#     def __init__(self,price,brand,camera):
#         print("inside the phone constructor")

#         self.__price = price
#         self.brand= brand
#         self.camera = camera
    
#     def show(self):
#         print(self.__price)


# class Smartphone(Phone):

#     def check(self):
#         print(self.__price)

# s= Smartphone(2000,"Apple",13)
# s.show()
        

class Person:
    def __init__(self, name, age):
        # Properties
        self.name = name
        self.age = age

    # Method to display person details
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Alice", 25)

# Accessing properties and methods
print(person1.introduce())


