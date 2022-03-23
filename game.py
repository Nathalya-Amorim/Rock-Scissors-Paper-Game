#Import packages to extend Python (just like we extend Sublime, Atom or VSCode)
from random import randint

# [] => this is an array
# name = [ value1, value2, value3]
# An array is a special type of container that can hold multiple items
# Arrays are indexed (their contents are assigned a number)
# the index always start at 0
choices = ["rock","paper","scissors"]

player_lives = 3
computer_lives = 3
total_lives = 3 

# Version 1, to explain array indexing
# player_choice = choices[1]
#print("index 1 in the choice array is " + player_choice + ", which is paper")

player_choice = input ("Choose rock, scissors, or paper: ")


print("user chose: " + player_choice)

#This will be the AI choice -> a random pick from the choices array
computer_choice = choices[randint (0, 2)]

print("computer chose: " + computer_choice)

if computer_choice == player_choice: 
	print("tie")

elif computer_choice == "rock":
	if player_choice == "scissors":
	   print("you lose!")
	   #verbose way
	   #player_lives = player_lives - 1
	   #simpliefied way
	   player_lives -= 1
	else:
		print("you win!")  
		computer_lives-= 1

elif computer_choice == "paper":
		if player_choice == "scissors":
			 print("you win!")
			 computer_lives-= 1
		else:
			 print("you lose!")
			 player_lives-= 1  

elif computer_choice == "scissors":
		if player_choice == "paper":
		   print("you lose!")
		   player_lives-= 1
		else:
		   print("you win!")
		   computer_lives-= 1 

print("Player lives:", player_lives)
print("Computer lives:", computer_lives)



