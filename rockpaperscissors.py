rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors."))
if user_choice >= 3 or user_choice < 0 :
  print("you typed invalid number") 
else:
        print(f"You chose:{game_images[user_choice]}")
        computer_choice= random.randint(0,2)
        print(f"Computer chose :\n{game_images[computer_choice]}")
        if user_choice == 0 and computer_choice == 2:
            print("You win!") 
        elif computer_choice>user_choice:
            print("you lose!")
        elif user_choice==computer_choice:
            print("Draw")
        elif user_choice == 2 and computer_choice == 0:  
            print("you lose!")
        elif computer_choice<user_choice:
            print("you Win!")  
