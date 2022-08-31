""" name = "Eric"
print(f"Hello {name.lower()}, this is your first!")
print(name.lower())
print(name.upper())
print(name.title())
 """


# author=" Nikola\t\nTesla "
""" message = f"{author.title()} once said, 'Be alone that is when ideas...'"
 print(message)
print(author.lstrip())
print(author.rstrip())
print(author.strip())"""


""" names= ['Ram', 'Sita', 'Hira', 'Gita']
print(f"I love {names[1].title()}") """

# motorcycles = ['Honda', 'Suzuki', 'BMW']
# print(motorcycles)
# motorcycles[0]= 'Ducati'
# motorcycles = []
# motorcycles.append('Ducati')
# motorcycles.append('Suzuki')
# motorcycles = ['Honda', 'Suzuki', 'BMW']
# del motorcycles[0]
# print(motorcycles) 

# Removing an item using the pop() method:
""" motorcycles = ['Honda', 'Suzuki', 'BMW']
print(motorcycles)
popped_motorcycles= motorcycles.pop()
print(motorcycles)
print(popped_motorcycles) """


#  inserting Elements into a list :
""" motorcycles = ['Honda', 'Suzuki', 'BMW']
motorcycles.insert(0, 'Ducati')
print(motorcycles)
 """

#  popping items from any position in a list
""" motorcycles = ['Honda', 'Suzuki', 'BMW']
first_owned = motorcycles.pop(0)
print(f"The first motorcyle I owned is {first_owned.title()}!")
print(motorcycles)
 """
# Removing an item by value
""" motorcycles = ['Honda', 'Suzuki', 'BMW']
motorcycles.remove('Honda')
print(motorcycles) """

""" motorcycles = ['Honda', 'Suzuki', 'BMW', 'Ducati']
too_expensive= 'Ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.upper()} is too expensive for me ") """

# 3-4:3-7 assignments

# guest_list = ['ram','Hira' , 'Sita' , 'Gita']
""" print(f"I would like to invite {guest_list[1].title()} to dinner!")
print(f"I would like to invite {guest_list[2].title()} to dinner!")
print(f"I would like to invite {guest_list[3].title()} to dinner!" """
""" guest_list[0] = 'Gyan'
guest_list.append('Raju')
guest_list.append('Paju')
guest_list.insert(0, 'Gobinda')
guest_list.insert(1, 'Ramesh') """
""" print(guest_list)
print(f"I would like to invite {guest_list} to the wedding") """
# person1= guest_list.pop(1)
# print(f"sorry {person1} that we could not invite you")
""" del guest_list[0]
print(guest_list)

 """
# Sorting a List permanently with the sort() method:



""" cars =['bmw','audi','mercedes']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars) """
# sorted() function :
""" cars = ['bmw','audi','mercedes']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:" )
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars) """

# Printing in reverse order :
""" cars = ['bmw','audi','mercedes']
cars.reverse()
print(cars) """

# Finding the length of a list:
""" 
cars = ['bmw','audi','mercedes']
print(len(cars)) """

# 3-8:
# my_locations = ['Hawai', 'Singapore','Dubai','India']
""" print(my_locations)
print(sorted(my_locations))
print(my_locations)
print(sorted(my_locations, reverse=True))
print(my_locations) """
""" my_locations.reverse()
my_locations.reverse()
my_locations.sort(reverse=True)
print(my_locations) """

# 3-9:
""" guest_list = ['ram','Hira' , 'Sita' , 'Gita']
number_guest= len(guest_list)
print(f"Hello I am invitng {number_guest} people to the party")
 """

#  for loops :
""" magicians = ['Alice' , 'David' , 'Christian']
for magician in magicians:
    # print(magician)
    print(f"{magician.upper()}, that was a great trick!")
    print(f"I cant wait to see your next trick, {magician.upper()}.\n")
print("Thank you everyone")  """ 

# 4-1
""" favourite_pizzas = ['Margherita' , 'Pepporoni', 'Cheese']
for fav_pizzas in favourite_pizzas:
    print(f"I love {fav_pizzas.upper()} pizza!!")
print("\nI really love pizzas!")     """

# 4-2
""" animals = ['Dog' ,'Cat', 'Mouse']
for animal in animals:
    # print(animal)
    print(f"A {animal.title()} would be a great pet")
print("\nAny of these animals would make a great pet!")    """

# range() function
""" for numbers in range(1,5):
    print(numbers)

value=list(range(1,5))
print(value) """
""" squares = []
for value in range(1,11,2):
    squares.append(value ** 2)
print(squares)
print(sum(squares))     """

""" in_list =[]
for values in range(0,31,3):
    in_list.append(values)
print(in_list) """
#  4-8

""" for value in range(1,11):
    cubes = value**3
    print(cubes)

 """
#  4-9 :
""" cubes = [value**3 for value in range(1,11)]
print(cubes)
 """

#  slicing a list :
""" players=['Ram','Hira','Sita','Shyam']
print(players[0:4]) """

#  Looping through a slice
""" players=['Ram','Hira','Sita','Shyam']
print("Here are the players of my team:")
for player in players[:4]:
    print(player)
 """

# Copying a list:
""" my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods) 
 """

#  4-10:
""" players = ['Ram','Hira','Sita','Shyam']
first_three = players[-3:]
print(f"First three players of the list are:\n{first_three}")
 """

# 4-11:
""" pizzas = ['Margherita' , 'Pepporoni', 'Cheese']
friend_pizzas = pizzas[:]

pizzas.append('Ham')
friend_pizzas.append('Paprika')

print("My favourite pizzas are:")
print(pizzas)
print("\nMy friends favourite pizzas are:")
print(friend_pizzas)
 """
# 4-12
""" my_foods = ['pizza', 'falafel', 'carrot cake']
for food in my_foods:
    print(food)
for my_fav_food in my_foods:
    my_fav_food = my_foods[1:]
print(f"These are my most favourites{my_fav_food}") """

# 4-13 :
""" buffet_foods = ('Daal','Bhaat','Icecream')
for food in buffet_foods:
    print(f"The items in menu are {food} ")
buffet_foods = ('Daal','Bhaat','Momo')    
for foodchange in buffet_foods:
    print(f"\nChange in menu are as follows {foodchange}")     """

# IF Statements:
# checking for equality
""" 
cars =['audi','bmw','mercedes','jaguar']
for car in cars:
    if car == 'bmw' :
        print(car.upper())
    else:
        print(car.title())     """

""" car = 'audi'
car == 'audi'
print(bool(car)) """

# checking for inequality :
""" requested_topping = 'Mushroom'
if requested_topping!= 'anchioves':
    print("Hold the anchovies!")
 """
# numerical comparisons :

""" answer = 17
if answer !=42 :
    print("This is it") """

# checking multiple conditions :
""" answer_1 = 22
answer_2 = 23
if answer_1 > 20 and answer_2 > 20 :
    print("Both are true")
 """
#  checking whether a value is in a list :
""" banned_users = ['Harry','Jack','Knight']
user= 'Maya'
if user not in banned_users:
    print(f"{user} you are invited!")

 """
# 5-1 :

""" car = 'subaru'
if car.title() == 'Subaru':
    print(car == 'subaru')
    print(car == 'Audi')
 """
 
""" requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!") """

# 5-3 : 5-4 
""" alien_color = 'orange'
if alien_color=='green':
    print("You just earned 5 points")
elif alien_color=='red':
    print("You just earned 15 points")    
elif alien_color=='orange':
    print("You just earned 10 points")     """

# 5-6 :
""" age = 65
if age < 2:
    print("The person is a baby")
elif age>=2 and age<4 :
    print("The person is a toddler")    
elif age>=4 and age<13 :
    print("The person is a kid")
elif age>=13 and age<20:
    print("The person is a teenage")
elif age>=20 and age<65:
    print("The person is an adult")    
else:
    print("The person is an elder")     """

# 5-7 :
""" favourite_fruits = ['Banana', 'Mango', 'Orange']
if 'Banana' in favourite_fruits:
    print("I really like bananas")
if 'Mango' in favourite_fruits:
    print('I really like Mangoes')    
if 'Apple' in favourite_fruits:
    print('I really like Apple')    
if 'Orange' in favourite_fruits:
    print('I really like Oranges')  """   

# checking for a special item in a list:
""" requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry we are out of Green Peppers.")
    else:
        print(f"Adding request toppings {requested_topping}") 
print("\nFinished making your pizza!")           
 """

# Checking that a list is not empty
""" requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}")
    print("\nFinished making your Pizza!")    
else:
    print("Are you sure you want a plain pizza?")     """

# using multiple lists :
""" available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry we don't have {requested_topping}")    
print("\nFinished making your pizza!")   """ 

# 5-8 :
""" usernames = ['Shyam', 'Admin' , 'Hari', 'Gita', 'Sita']
for username in usernames:
    if username=='Admin':
        print(f"Hello {username} would you like to see the report")
    else :
        print(f"Hello {username} thank you for logging in again")   
 """
#  5-9 : 
""" usernames = []
if usernames:
    for username in usernames:
        print("We have lot of users")
else:
    print("We need to find some users")        
 """
# 5-10:
""" currentusernames = ['Shyam', 'Admin' , 'Hari', 'Gita', 'Sita']
currentusernames!=['shyam', 'admin' , 'hari', 'gita', 'sita'] 
new_usernames = ['Jack', 'admin' , 'Dowsey', 'Austin', 'sita']
for new_username in new_usernames:
    if new_username in currentusernames:
        print(f"Sorry the username {new_username} is already taken")
    else:
        print(f"The username {new_username} is available")     """

# 5-11 :
""" my_lists= [*range(1,10)]
for my_list in my_lists:
    if my_list== 1:
        print(f"{my_list}st")
    elif my_list==2:
        print(f"{my_list}nd")  
    elif my_list==3:
        print(f"{my_list}rd") 
    else:
        print(f"{my_list}th")   """       

# Dictionaries : 
""" alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_pts = alien_0['points']
print(f"you have just earned {new_pts} points")
 """
# adding new key-value pairs :
""" alien_0 = {'color':'green','points':5}
del alien_0['points'] 
print(alien_0)
 """
# modifying values in a dictionary
""" alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original value : {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':   
    x_increment = 2
else:
    x_increment = 3    
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position :{alien_0['x_position']}")
 """
# A dictionary of similar objects:
""" favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title() 
print(f"Sarah's favourite language is {language}") """

# get():
""" alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('temp', )
print(point_value) """

# 6-1 
""" brother_sus={
    'firstname':'Sushant' ,'lastname':'Basnet', 'age':25,
    'city':'damak'
    }
print(brother_sus['firstname'])
print(brother_sus['lastname'])    
print(brother_sus['age'])    
print(brother_sus['city'])     """

# 6-2 
""" favorite_numbers = {
    'jen': '7',
    'sarah': '21',
    'edward': '33',
    'phil': '8',
    }
person = favorite_numbers['jen']
print(f"Jen's favourite number is {person}")   
 """

# looping through dictionaries
""" user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key,value in user_0.items():
    print(f"\nKey: {key}") 
    print(f"Value: {value}")
         """
""" favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }       
for name,language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")
     """
    
#Looping through all the keys in a dictionary:
""" favorite_languages ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
for name in favorite_languages.keys():  #can also work without keys()
    print(name.title())   """
""" favorite_languages ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if 'erin' not in favorite_languages.keys():
        print("Erin please take the poll") """

# 6-4:
""" rivers_origin = {
    'nile': 'africa',
    'amazon': 'brazil',
    'ganges':'india'
    }
for river, country in rivers_origin():
    print(f"The {river.title()} river runs through {country.title()}") """

# 6-5 :
""" rivers_origin = {
    'nile': 'africa',
    'amazon': 'brazil',
    'ganges':'india'
    }
for river in rivers_origin:
    print(f"The {river.title()} river") """
""" rivers_origin = {
    'nile': 'africa',
    'amazon': 'brazil',
    'ganges':'india'
    }
for country in rivers_origin.values():
    print(f"The {country.title()} ") """

#6-6 :
""" favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    } 
names_1= {'sarah','phil','Alex','Ram'}
for name in favorite_languages.keys():
    if name in names_1:
        language = favorite_languages[name].title()
        print(f"Thanks for the poll {name.title()} your answer:{language}")
    if name not in names_1:
        print(f"Invited to the poll {name.title()} ")
         """

# Nesting :


   
