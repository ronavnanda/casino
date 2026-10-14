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

#create a function to deal cards
def deal_card():
  global aces
  #random.choice(nums_array) is same as nums_array[random.randint(0,21)]
  cardValue = random.choice(nums_array)
  card = str(cardValue)
  if cardValue == 11:
    card = "Jack"
    cardValue = 10
  if cardValue == 12:
    card = "Queen"
    cardValue = 10
  if cardValue == 13:
    card = "King"
    cardValue = 10
  if cardValue == 14:
    card = "Ace"
    cardValue = 11
    aces += 1
  return card, cardValue


#set playing to yes
playing = "Y"

#game...
while playing.lower() == "y":

  aces = 0
  busted = False

  #getting cards 1 and 2
  card1, card1Number = deal_card()
  card2, card2Number = deal_card()

  playerSum = card1Number + card2Number

  if playerSum > 21:
    playerSum -= 10
    aces -= 1

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

    card, cardNumber = deal_card()

    #ensure Ace is worth 1 instead of 11 to avoid going bust.
    if cardNumber == 11 and playerSum > 10:
      cardNumber = 1
      aces -= 1

    playerSum += cardNumber

    while aces > 0 and playerSum > 21:
      aces -= 1
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
    aces = 0
    print("Now it is time for the dealer!")
    dealerCard1, dealerCard1Value = deal_card()
    dealerCard2, dealerCard2Value = deal_card()
    
    dealerSum = dealerCard1Value + dealerCard2Value

    if dealerSum > 21:
      dealerSum -= 10
      aces -= 1


    if dealerSum > 16:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to stand")
    while dealerSum<17 and dealerSum<playerSum:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to hit")
      print("dealer is hitting...")

      dealerCard, dealerCardValue = deal_card()
      
      if dealerCardValue == 11 and dealerSum > 10:
        dealerCardValue = 1
        aces -= 1

      dealerSum += dealerCardValue

      while aces > 0 and dealerSum > 21:
        aces -= 1
        dealerSum -= 10

      print(f"Dealer got a {dealerCard}. Total sum is now {dealerSum}")
      if dealerSum > 21:
        print("Dealer busted")

    if(playerSum>dealerSum or dealerSum>21):
      print("You won!")
    elif(playerSum==dealerSum):
      print("It's a tie")
    else:
      print("You lost")

  playing = input("Would you like to continue playing? (Y/N): ")
  while playing.upper() != "Y" and playing.upper() != "N":
    print("Invalid input. Please enter Y or N.")
    playing = input("Would you like to continue playing? (Y/N): ")
