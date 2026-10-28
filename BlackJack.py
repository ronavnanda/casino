#Blackjack
import random

#set array of numbers to choose from
nums_array = [
    2,3,4,5,6,7,8,9,10,
    11,11,11,11,
    12,12,12,12,
    13,13,13,13,
    14
]

#this is the dictionary
card_names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"} 

#create a function to deal cards
def deal_card(aceCount):
  cardValue = random.choice(nums_array) #get a value from the array
  if cardValue == 14:
    aceCount += 1
  card = card_names.get(cardValue, str(cardValue)) #this is .get() which looks for a key in the dictionary. str(cardValue) is returned when key isn't found
  cardValue = 10 if cardValue in (11,12,13) else 11 if cardValue == 14 else cardValue #compact way to write if/else logic
  return card, cardValue, aceCount

def determineWinner():
  if(playerSum>dealerSum or dealerSum>21):
      return "You won!"
  elif(playerSum==dealerSum):
      return "It's a tie"
  else:
      return "You lost"

#set playing to yes
playing = "Y"

#game...
while playing.lower() == "y":

  aceCount = 0
  busted = False

  #getting cards 1 and 2
  card1, card1Number, aceCount = deal_card(aceCount)
  card2, card2Number, aceCount = deal_card(aceCount)

  playerSum = card1Number + card2Number

  if playerSum > 21:
    playerSum -= 10
    aceCount -= 1

  print(f"Your first card is {card1} and your second card is {card2}! Your total is {playerSum}.")

  hitting = input("Would you like to hit? (Y/N): ")

#dealing with improper inputs
  while hitting.lower() != "y" and hitting.lower() != "n":
    print("Invalid input. Please enter Y or N.")
    hitting = input("Would you like to hit?: ")

#output if not hitting
  if hitting.lower() == "n":
    print("You chose to stand")

#while hitting logic
  while hitting.lower() == "y":
    hitting = "n";
    print("You are hitting...")

    card, cardNumber, aceCount = deal_card(aceCount)

    playerSum += cardNumber

    #if sum is greater than 21, and they have an ace, make the ace worth 1 instead of 11
    while aceCount > 0 and playerSum > 21:
      aceCount -= 1
      playerSum -= 10

    print(f"Your card is {card}! Your total is now {playerSum}.")

    #determine if busted or not, determine if user will continue to hit.
    if playerSum>21:
      print("You busted")
      busted = True;
    elif playerSum==21:
      hitting = "n"
    else:
      hitting = input("Would you like to hit? (Y/N): ")

  #dealer setup
  if(busted != True):
    aceCount = 0
    print("Now it is time for the dealer!")
    dealerCard1, dealerCard1Value, aceCount = deal_card(aceCount)
    dealerCard2, dealerCard2Value, aceCount = deal_card(aceCount)

    dealerSum = dealerCard1Value + dealerCard2Value

    if dealerSum > 21:
      dealerSum -= 10
      aceCount -= 1


    if dealerSum > 16:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to stand")
    while dealerSum<17:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to hit")
      print("dealer is hitting...")

      #get dealer their card
      dealerCard, dealerCardValue, aceCount = deal_card(aceCount)

      dealerSum += dealerCardValue

      while aceCount > 0 and dealerSum > 21:
        aceCount -= 1
        dealerSum -= 10

      print(f"Dealer got a {dealerCard}. Total sum is now {dealerSum}")
      if dealerSum > 21:
        print("Dealer busted")

    print(determineWinner())

  playing = input("Would you like to continue playing? (Y/N): ")
  while playing.upper() != "Y" and playing.upper() != "N":
    print("Invalid input. Please enter Y or N.")
    playing = input("Would you like to continue playing? (Y/N): ")
