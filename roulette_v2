import random

name = input("Enter your name: ")
#ID = random.randint(0,1000)
cashInitial = 1000
cash = 1000
playing = True
print(f"Hello " + name + " and welcome to the casino! You have " + str(cash) + " dollars") #no println

while playing and cash > 0:
  numUpredict = int(input(f"Choose an integer between 0 and 36 (inclusive): ")) #wrapping the string to an integer
  while numUpredict>36 or numUpredict<0:
    numUpredict = int(input(f"{numUpredict} is not between 0 and 36 (inclusive). Please choose an integer between 0 and 36: "))

  spend = int(input(f"How much of your cash would you like to spend?: "))
  while(spend>cash):
    print(f"You do not have enough cash")
    spend = int(input(f"How much of your cash would you like to spend? Needs to be less than or equal to " + str(cash) + " :"))

  #print("Your ID is " + str(ID)) # cant have numbers and strings... so instead of "..." + 5, maybe ID = 5 and do "..." + ID. NVM you need to do +str(ID) or +str(5)
  numberRolled = random.randint(0,36)
  print(f"Your spin is " + str(numberRolled))

  #adding if won or subtracting if lose
  if numUpredict==numberRolled:
    cash = cash + spend*35
    print(f"You won! Congrats player {name}. Your cash value is now {cash}.") #if u put the f in the front then u can do strings numbers etc! instead of str() each time
  else:
    cash = cash - spend
    print(f"You lost xD, your cash value is now {cash}.")

  var = input(f"would you like to continue? (Y/N): ")

  if var.upper() == "N":
    playing = False


if(cash>=cashInitial):
  print("Goodbye!")
else:
  print("Bye sucker xD")
