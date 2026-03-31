
import random

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

game_images=[rock, paper, scissors]

human_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))

if human_player >= 0 and human_player <=2:
    print(game_images[human_player])


computer = random.randint(0,2)
print("Computer chose: ")
if computer >= 0 and computer <=2:
    print(game_images[computer])



if computer == 2 and human_player == 1:
    print("Computer wins!!")
elif computer == 1 and human_player == 2:
    print("You win!!!")
elif computer == 0 and human_player == 1:
    print("You win!!!")
elif computer == 1 and human_player == 0:
    print ("Computer wins!!!!")
elif computer == 0 and human_player == 2:
    print ("Computer wins!!!!")
elif computer == 2 and human_player == 0:
    print ("You win!!!!")
elif computer == 1 and human_player == 2:
    print ("You win!!!!")
elif computer == human_player:
    print ("It's a draw!!!!")
else:
    print("That's not an option, you lost!")



