from random import randint


choices = ["rock island","paper island","scissors island"]

visitor_bells = 3
tom_nook_bells = 3
total_bells = 3

visitor_choice = False


def winorlose(status):
	
	print("You",status,"! Would like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Come to visit us again next time")
		exit()
	elif choice == "Y" or choice == "y":
		
		global visitor_bells
		global tom__nook_bells
		global total_bells
		visitor_bells = total_bells
		tom_nook_bells = total_bells
	else:
	    print("Make a valid choice - Y or N")
	    #this might generate a bug that we need to fix later
	    choice = input("Y / N? ")

#player_choice == False
while visitor_choice is False: # = True
	print("==================*/ RPS GAME */=================")
	print("Tom Nook Bells:", tom_nook_bells,"/", total_bells)
	print("Visitor Bells:", visitor_bells,"/", total_bells)
	print("==================================")
	#Version 1, to explain array indexing
	# player_choice = choices[1]
	#print("index 1 in the choice array is " + player_choice + ", which is paper")

	print("Choose your island to earn or lose some bells! Or type quit to exit \n")

	visitor_choice = input ("Choose rock island, scissors island, or paper island: \n")
	#player_choice now equals TRUE -> It has a value.

	if visitor_choice == "quit":
	   print("You chose to quit")
	   exit()

	print("user chose: " + visitor_choice)

	#This will be the AI choice -> a random pick from the choices array
	tom_nook_choice = choices[randint (0, 2)]

	print("Tom Nook chose: " + tom_nook_choice)

	if tom_nook_choice == visitor_choice: 
		print("tie")

	elif tom_nook_choice == "rock island":
		if visitor_choice == "scissors island":
		   print("you lose a bells!")
		   #verbose way
		   #player_lives = player_lives - 1
		   #simpliefied way
		   visitor_bells -= 1
		else:
			print("You WIN.You do not lose a bell")  
			tom_nook_bells-= 1

	elif tom_nook_choice == "paper island":
			if visitor_choice == "scissors island":
				 print("You WIN. You do not lose a bell!")
				 tom_nook_bells-= 1
			else:
				 print("you lose a bell!")
				 visitor_bells-= 1  

	elif tom_nook_choice == "scissors island":
		if visitor_choice == "paper island":
			print("you lose a bell!")
			visitor_bells-= 1
		else:
			print("You WIN! You do not lose a bell!")
			tom_nook_bells-= 1 

	if visitor_bells == 0:
		winorlose("lose")
	  
	if tom_nook_bells == 0:
		winorlose("won")

	print("Your bells:", visitor_bells)
	print("Tom Nook's bells:", tom_nook_bells)

	# map the loop keep running, by setting player_choice back to False
	# uset, so that our loop condition will evaluate to True
	visitor_choice = False



