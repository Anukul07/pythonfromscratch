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

#  




