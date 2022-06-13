# lets play rock, paper, scissors

import random

from random import choice, random

while True: 

 user_input = input ("Enter your choice ('r', 'p', 's') "). lower()

 if user_input == "rock":
     user_action = "rock"

 elif user_input == "p":
     user_action = "paper"

 elif user_input == "s":
     user_action = "scissors"

 else:
     print("Invalid input entered, try again") 

 player_action = ["rock", "paper", "scissors"]   
 CPU_action = choice(player_action)

 print(f"\nplayer {user_action}, computer chose {CPU_action}.\n")  

 if user_action == CPU_action:
      print (f"Both players selected {user_action}. It's a tie!") 

 elif user_input == "rock":
     if CPU_action == "scissors":
        print("rock smashes scissors! You win!")  
     else :
         print("Paper covers rock! You lose.") 

 elif user_action == "paper":
        if CPU_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")

 elif user_action == "scissors":
        if CPU_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.") 
           


  
 
