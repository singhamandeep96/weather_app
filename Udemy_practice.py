## Problem 1
# print("Welcome to the rollercoaster!")
# height=int(input("What is your height in cm ?"))
# bill=0

# if height >=120:
#     print("You can ride the rollercoaster")
#     age=int(input("What is your age ?"))
#     if(age <=12):
#         bill=5
#         print("Child tickets are $5.")
#     elif age <=18:
#         bill=7
#         print("Youth tickets are $7.")
#     else:
#         bill=12
#         print("Adult tickets are $12.")

#     wants_photo=input("Do you want to have a photo take ? Type y for yes and n for no")
#     if wants_photo=="y":
#         bill+=3

#     print(f"Your final bill is {bill}")

# else:
#     print("Sorry you have to come taller before you can ride.")



##Problem 2

# print ("Welcome to Python Pizza Deliveries!")
# size= input("What size pizza do you want? S, M or L: ")
# pepperoni= input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese= input("Do you want extra cheese? Y or N: ")

# bill=0

# if (size=='S'):
#     bill=15
    

# elif (size=='M'):
#     bill=20
    

# else:
#     bill=25
     


# if pepperoni== "Y":
#     if size== "S":
#         bill+=2
#     else:
#         bill+=3


# if extra_cheese== "Y":
#     bill+=1

# print(f" Your final bill is: ${bill}") 


## General Practice

import random

# random_integer = random.randint(1,10)
# print(random_integer)


# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)


# random_heads_or_tails = random.randint(0, 1)
# if (random_heads_or_tails==0):
#     print("Heads")

# else:
#     print("Tails")


# import random 
# friends= ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# #1st option
# print(random.choice(friends))

# #2nd option
# random_index= random.randint(0, 4)
# print(friends[random_index])


## For Loop

# fruits =["Apple" , "Peach", "Pie" ]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruits)

# student_scores= [150, 142, 185, 120, 171, 184, 149, 24,59, 68, 199, 78, 65, 89, 86]

# max_score= 0
# for score in student_scores:
#     if score > max_score:
#         max_score= score
    
# print(max_score)

# sum=0
# for number in range(1, 101):
#     sum= sum +number

# print(sum)

### Hangman Game
# import random 
# word_list=["aardvark", "baboon", "camel"]

# chosen_word= random.choice(word_list)
# print(chosen_word)

# placeholder= ""
# word_length=len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)


# #TODO-1 :- Use a while loop to let the user guess again.

# game_over = False
# correct_letters=[]

# while not game_over:
#     guess= input("Guess a letter: ").lower()

#     display = ""



# # TODO-2 : Change the for loop so that you keep the previous correct letters in display.

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#         correct_letters.append(guess)
#     elif letter in correct_letters:
#         display += letter
#     else:
#         display +="_"

# print(display)


def greet():
    print("Hello")
    print("Kidda")
    print("Namaste") 

greet()     