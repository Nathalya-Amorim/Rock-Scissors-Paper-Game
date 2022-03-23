#Import packages to extend Python (just like we extend Sublime, Atom or VSCode)
from random import randint

print ("Let's start the game")

choices = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

computer_choice = choices[randint (0, 8)]

print("computer chose card number:  " + str computer_choice)

print("The next card is greater or less than  " + computer_choice)


