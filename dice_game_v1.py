#Dice Game Get it greater than a number
import random

count = 0

#set up basics
name = input("What is your name? ")

#forces input to be an integer
numToWin = int(input(f"Welcome {name}! Which number do you hope to roll equal to or more? (1-6) "))
while numToWin <= 0:
  numToWin = int(input("Please enter a number greater than 0: "))
while numToWin >= 7:
  numToWin = int(input("Please enter a number less than 7: "))

#Welcome player
print(f"You are trying to roll a number greater than or equal to {numToWin}.")
numberOfRolls = int(input("How many times would you like to roll? (100 max) "))
while numberOfRolls > 100:
  numberOfRolls = int(input("Please enter a number less than or equal to 100: "))
while numberOfRolls < 1:
  numberOfRolls = int(input("Please enter a number greater than 0: "))

expectedWins = int((7 - numToWin) / 6 * numberOfRolls)
print(f"Expected wins: {expectedWins:.0f}")

#roll the dice
for i in range(numberOfRolls):
  x = random.randint(1,6)
  print(f"You rolled a {x}.")
  if x>=numToWin:
    count += 1

if(count>expectedWins):
  statement = "You got lucky!"
elif(count<expectedWins):
  statement = "You got unlucky..."
else:
  statement = "Your result was expected."
print(f"You won {count} times. You were expected to win {expectedWins:.0f} times. {statement}")
  
