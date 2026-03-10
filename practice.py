# print ("Hello world")  ## Question 1

# a=10    ## Question 2
# b=5
# print(a+b)


# a = int(input("Enter a number"))  ##Question 3
# print(a*a)

# b= int(input("Enter base of triangle"))
# h= int(input("Enter height of triangle"))

# area= 1/2*b*h                   ##Question 4 
# print("Area of triangle is :", area) 


# a=int(input("Enter first number: "))  ##Question 6
# b=int(input("Enter second number: "))

# temp=a  
# a=b
# b=temp

# print(f"After swapping the numbers first number={a}, second number={b}")

# import random   ## Question 7

# a= (random.randint(0,10))

# print(a)

# a=int(input("Enter number in kms: "))  ## Question 8

# miles= a*0.62

# print(f"{a} kms is: {miles} miles")

# c= int(input("Enter temp in celcius: ")) ## Question 9

# f= c*(9/5) + 32

# print(f"{c} celcius is {f} farenheit")


# a=int(input("Enter a number: "))  ## Question 10

# if(a>0):
#     print("a is positive")

# elif (a<0):
#     print("a is negative")

# elif(a==0):
#     print("a is 0")


# a=int(input("Enter a number: ")) ##Question 11

# if(a%2==0):
#     print("Number is even")
# else:
#     print("Number is odd")


# y=int(input("Enter year: "))  ##Question 12

# if(y%4==0):
#     print(f"{y} is a leap year")

# else:
#     print(f"{y} is not a leap year")

# a=int(input("Enter first number: "))   ##Question 13
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))

# if(a>b and a>c):
#     print(f"{a} is largest")

# elif(b>a and b>c):
#     print(f"{b} is greatest")

# else:
#     print(f"{c} is greatest")


# a=int(input('Enter a number:'))  ##Question 14

# c=0

# for i in range(2,(a-1)):
#     if(a%i==0):
#         c=c+1
#         break

# if c==0:
#     print(f"{a} is a prime number")

# else:
#     print(f"{a} is not a prime number") 


   
# a=int(input("Enter first number: "))  ##Question 15
# b=int(input("Enter second number"))


# for i in range(a,b):
#     c=0
#     for j in range(2,(i-1)):
#         if(i%j==0):
#             c=c+1
#             break
#     if(c==0):
#         print(i)


# n=int(input("Enter a number: "))  ##Question 16

# product=1
# for i in range(1, n+1):
#     product=product*i

# print(f"The factorial of {n} is {product}")


# n=int(input("Enter a number: ")) #Question 17

# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")


# import math        ##Question 

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))

# x1= (-b+ math.sqrt(b*b -4*a*c))/2*a
# x2=(-b- math.sqrt(b*b -4*a*c))/2*a

# print(f"The values of x1 and x2 for the equation are {x1} and {x2} ")



## practice question 

# def print_num(*args):
#     for number in args:
#         print(number)

# print(print_num(1,2,3,4,5,6, "Amandeep"))


##Practice question
# def print_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")



# print_details(name="Amandeep", age=28, city="Delhi")



##Practice question 

def print_values(*args, **kwargs):
    for value in args:
        print(f"Positional Argument {value}")

    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_values(1,2, 3 ,4, 5, name="Amandeep", age=21, city="Delhi"  )






    








    