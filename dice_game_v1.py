#Dice Game Get it greater than a number
import random

nameS = "Classic"
x = random.randint(1,6)
ID = 5
numToWin = 5

print("Hello " + nameS + " and welcome to the Ave Casino!") #no println
print("Your ID is " + str(ID)) # cant have numbers and strings... so instead of "..." + 5, maybe ID = 5 and do "..." + ID. NVM you need to do +str(ID) or +str(5)
print("You are trying to roll a number greater than or equal to " + str(numToWin) + ".")
print("Your first roll is " + str(x))

if x>=numToWin:
  print(f"You won! Congrats player {ID}") #if u put the f in the front then u can do strings numbers etc! instead of str() each time
else:
  print("You lost xD")

count = 0
while x<numToWin:
  count += 1 #no count++
  x = random.randint(1,6)
  print("   You just rolled a " + str(x))

if count>0:
  print(f"It took {count} more roll(s) to win! Congrats player {ID}")
