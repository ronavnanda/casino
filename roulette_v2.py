import random

name = input("Enter your name: ")
cashInitial = int(input("How much cash do you want to start with? ")) #input normally gets as a string so add int() at front to get as integer
cash = cashInitial
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

  numberRolled = random.randint(0,36)
  print(f"Your spin is " + str(numberRolled))

  #adding if won or subtracting if lose
  if numUpredict==numberRolled:
    cash = cash + spend*35
    print(f"You won! Congrats player {name}. Your cash value is now {cash}.") #if u put the f in the front then u can do strings numbers etc! instead of str() each time
  else:
    cash = cash - spend
    print(f"Your cash value is now {cash}.")

  if cash == 0:
    break
  else:
    var = input(f"would you like to continue? (Y/N): ").upper()

    while var != "Y" and var != "N":
      print("Invalid input. Please enter Y or N.")
      var = input(f"would you like to continue? (Y/N): ").upper()

    if var == "N":
      playing = False


if(cash>=cashInitial):
  print("Goodbye!")
else:
  print("You lost xD")
