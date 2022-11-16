""" import random
import mymodule
random_integer = random.randint(0,100)
print(random_integer)
 """

""" import random
random_Integer = random.randint(0,1)
if random_Integer == 1:
    print("Heads")
else:
    print("Tails")    """ 
""" 

import random
names_string = input("Give me everybody's names, seperated by a comma.")
names = names_string.split(", ")
print(f"{names_string}")
random_number = random.randint(0,5)
if random_number == 1:
    print(f"{names[0]}, you will have to pay the bill!")
elif random_number == 2 :    
    print(f"{names[1]}, you will have to pay the bill!")
elif random_number == 3 :    
    print(f"{names[2]}, you will have to pay the bill!")
elif random_number == 4 :    
    print(f"{names[3]}, you will have to pay the bill!")
else:    
    print(f"{names[4]}, you will have to pay the bill!")
 """

# # picking the person who pays the bill : 
# import random
"""
names_string = input("Enter the names of people seperated by commas")
names = names_string.split(", ")
num_of_people = len(names)
random_choice = random.randint(0,num_of_people - 1)
person_who_will_pay = names[random_choice]                            #can use this or the one below
print(person_who_will_pay + " You will have to pay the bill") """

# alt : 
""" picked_person = random.choice(names)
print(f"{picked_person}, you will have to pay the bill")
 """

""" fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3]) """

""" student_heights=input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights) 
#sum function by using for loop:
total_height = 0
for height in student_heights:
    total_height+=height
print(total_height)
# len function by using for loop 
number_of_students = 0
for student in student_heights:
    number_of_students+=1
print(number_of_students)    
 """

# Highest score exercise :
""" student_scores = input("Input a list of student det scores").split()
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)    
heighest_score = 0 
for score in student_scores:
    if score > heighest_score:
        heighest_score= score

print(f"The height score of the class is {heighest_score}!")        
 """
""" sum_even = 0
for sum in range(2,101,2):
    sum_even += sum
print(sum_even)    
     """

""" for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0 :
        print("Fizz")
    elif number % 5 == 0 :
        print("Buzz")
    else: 
        print(number)          
 """
# functions with more than 1 input :
""" def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Jack Bauer" , "Nowhere")     """

# keyword arguments :
""" def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with(location ="nowhere" , name ="angela")    
 """

