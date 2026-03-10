# def welcome():
#     return "Welcome to the advanced python class"

# welcome()

# wel= welcome
# print(wel())
# del welcome
# print (wel())


##closure functions 

# def main_welcome(msg):

#     def sub_welcome_method():
#         print("Welcome to advanced python course")
#         print(msg)
#         print("please learn these concepts properly")

#     return sub_welcome_method()

# main_welcome("Welcome everyone")


# def main_welcome(func):

#     def sub_welcome_method():
#         print("Welcome to the advanced python course ")
#         func("Welcome everyone to this tutorial")
#         print("please learn these concepts properly")

#     return sub_welcome_method()

# main_welcome(print)


# def main_welcome(func,lst):
    
#     def sub_welcome_method():
#         print("Welcome to the advanced python course")
#         print(func(lst))
#         print("Please learn these concepts carefully")
#     return sub_welcome_method()

# main_welcome(len,[1,2,3,4,5])


## Decorators

# def main_function(func):

#     def sub_function():
#         print("Welcome to the the python course")
#         func()
#         print("Please learn these concepts properly")

#     return sub_function()

# def course_introduction():
#     print("This is advanced python course")

# course_introduction()


# main_function(course_introduction)


# @main_function
# def course_introduction():
#     print("This is advanced python course")



# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called")
#         func()
#         print("Something is happening after the function is called")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()


# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hello():
#     print("Hello")

# say_hello()



   