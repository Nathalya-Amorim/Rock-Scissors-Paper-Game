from gameComponents import gameVars

#define a win or lose function
def winorlose(status):
	#version1 of function
	#print("Inside winorlose function; status is: ",status)
	print("You",status,"! Would like to play again?")
	choice = input("Y / N? ")

	if choice == "N" or choice == "n":
		print("You chose to quit! Better luck next time")
		exit()
	elif choice == "Y" or choice == "y":
		#reset the player lives and computer lives
		#and reset player choice to False, so our loop restarts
		global player_lives
		global computer_lives
		global total_lives
		gameVars.player_lives = gameVars.total_lives
		gameVars.computer_lives = gameVars.total_lives
		gameVars.player_choice = False
	else:
	    print("Make a valid choice - Y or N")
	    #this might generate a bug that we need to fix later
	    choice = input("Y / N? ")