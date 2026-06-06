import random

name = input("Enter your name: ")
ID = random.randint(1,1000)
y = random.randint(0,36)

print("Hello " + name + " and welcome to the casino!") #no println
x = int(input("Choose an integer between 0 and 36 (inclusive): ")) #wrapping the string to an integer
while x>36 or x<0:
  x = int(input(f"{x} is not between 0 and 36 (inclusive). Please choose an integer between 0 and 36: "))
print("Your ID is " + str(ID)) # cant have numbers and strings... so instead of "..." + 5, maybe ID = 5 and do "..." + ID. NVM you need to do +str(ID) or +str(5)
print("Your first spin is " + str(y))

if x==y:
  print(f"You won in one try! Congrats player {ID}") #if u put the f in the front then u can do strings numbers etc! instead of str() each time
else:
  print("You lost xD")

count = 0
while x!=y:
  count += 1 #no count++
  y = random.randint(0,36)
  print("   You just spun a " + str(y))

if count>0:
  print(f"It took {count} more spin(s) to win! Congrats player {ID}")
