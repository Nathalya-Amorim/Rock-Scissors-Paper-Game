from random import radint

choices = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

computer_choice = choices [radint (0, 8)]

player_choice = input ( " Choose a number between 1 and 9 :  " )

print ( "user chose:  " + player_choice)

