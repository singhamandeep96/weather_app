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



# def convert_temperature(temp, unit):
#     if unit=='C':
#         return temp * 9/5 + 32
    
#     elif unit=='F':
#         return (temp-32)*5/9 
    
#     else:
#         return None
    
# print(convert_temperature(55, 'F'))



# def is_palimdrome(s):
#     s=s.lower().replace(" ","")
#     return s==s[::-1]

# print(is_palimdrome("Aman"))
# print(is_palimdrome("Nano"))


# addition= lambda a,b: a+b

# print(addition(2,5))


# multiply= lambda a,b,c:a*b*c

# print(multiply(2,5,7))

# numbers= [1,2,3,4,5,6,7,8,9]

# s=list(map(lambda x:x**2, numbers))

# print(s)


# words=['apple', 'banana', 'pineapple']
# upper_words= list(map(str.upper, words))
# print(upper_words)


# numbers=[1,2,3,4,5,6,7,8,9,0]

# greater_than_five= list(filter(lambda x : x>5, numbers))

# print(greater_than_five)


# lst=[2,4,5,6,3,2,67,78]

# even_greater_than_five= list(filter(lambda x: x>5 and x%2==0, lst))

# print(even_greater_than_five)



# people=[
#     {'name':'Krish','age':32},
#     {'name':'Jack','age':33},
#     {'name':'John','age':25}
# ]

# age_greater_than_25= list(filter(lambda x: x['age']>25, people))

# print(age_greater_than_25)


# lst1=[]

# def lst_square(lst):
#     for i in lst:
#         lst1.append(i*i)

#     return lst1

# print(lst_square([1,2,3,4,5,6,7,8,9]))


list=[1,2,3,4,5,6,7,8,9]

lst2= [i*i for i in list if i%2==0]
print(lst2)
