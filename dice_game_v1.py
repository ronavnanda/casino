#Dice Game Get it greater than a number
import random

#set up basics
name = input("What is your name? ")
numToWin = 5
count = 0

#Welcome them to casino
print(f"Hello {name} and welcome to the Ave Casino!") 
print(f"You are trying to roll a number greater than or equal to {numToWin}.")

#roll the dice
x = random.randint(1,6)
print(f"Your first roll is {x}.")

#determine if player has won
if x>=numToWin:
  print(f"You won! Congrats {name}") 
else:
  print("You lost xD")

#add a counter to track loss streak
while x<numToWin:
  count += 1 #no count++
  x = random.randint(1,6)
  print("You just rolled a " + str(x))

if count>0:
  print(f"It took {count} more roll(s) to win! Congrats player {ID}")
