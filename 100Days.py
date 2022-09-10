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

# picking the person who pays the bill : 
import random
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

