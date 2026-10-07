#Blackjack
import random

#set array of numbers to choose from
nums_array = [2,3,4,5,6,7,8,9,10,11,11,11,11,12,12,12,12,13,13,13,13,14]

#set playing to yes
playing = "Y"

#game...
while playing.lower() == "y":

  busted = False

  #getting cards 1 and 2
  card1ArrayPosition = random.randint(0,21)
  card2ArrayPosition = random.randint(0,21)
  card1Number = nums_array[card1ArrayPosition]
  card2Number = nums_array[card2ArrayPosition]

  #set card numbers to the card name
  card1 = str(card1Number)
  card2 = str(card2Number)

  #setting face cards to their proper value (ex: number 11 --> Jack)
  if card1Number == 11:
    card1 = "Jack"
    card1Number = 10
  if card1Number == 12:
    card1 = "Queen"
    card1Number = 10
  if card1Number == 13:
    card1 = "King"
    card1Number = 10
  if card1Number == 14:
    card1 = "Ace"
    card1Number = 11

  #now for 2nd card
  if card2Number == 11:
    card2 = "Jack"
    card2Number = 10
  if card2Number == 12:
    card2 = "Queen"
    card2Number = 10
  if card2Number == 13:
    card2 = "King"
    card2Number = 10
  if card2Number == 14:
    card2 = "Ace"
    card2Number = 11

  playerSum = card1Number + card2Number

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
    cardNumber = nums_array[random.randint(0,21)]

    card = cardNumber
    if cardNumber == 11:
      card = "Jack"
      cardNumber = 10
    if cardNumber == 12:
      cardName = "Queen"
      cardNumber = 10
    if cardNumber == 13:
      cardName = "King"
      cardNumber = 10
    if cardNumber == 14:
      cardName = "Ace"
      cardNumber = 11

    playerSum += cardNumber

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
    print("Now it is time for the dealer!")
    dealerCard1Number = nums_array[random.randint(0,21)]
    dealerCard2Number = nums_array[random.randint(0,21)]
    
    dealerCard1 = str(dealerCard1Number)                
    if dealerCard1Number == 11:
      dealerCard1 = "Jack"
      dealerCard1Number = 10
    if dealerCard1Number == 12:
      dealerCard1 = "Queen"
      dealerCard1Number = 10
    if dealerCard1Number == 13:
      dealerCard1 = "King"
      dealerCard1Number = 10
    if dealerCard1Number == 14:
      dealerCard1 = "Ace"
      dealerCard1Number = 11

    dealerCard2 = str(dealerCard2Number)
    if dealerCard2Number == 11:
      dealerCard2 = "Jack"
      dealerCard2Number = 10
    if dealerCard2Number == 12:
      dealerCard2 = "Queen"
      dealerCard2Number = 10
    if dealerCard2Number == 13:
      dealerCard2 = "King"
      dealerCard2Number = 10
    if dealerCard2Number == 14:
      dealerCard2 = "Ace"
      dealerCard2Number = 11
  
    dealerSum = dealerCard1Number + dealerCard2Number

    if dealerSum > 16:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to stand")
    while dealerSum<17 and dealerSum<playerSum:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to hit")
      print("dealer is hitting...")
      dealerCardNumber = nums_array[random.randint(0,21)]
      dealerCard = str(dealerCardNumber)
                        
      if dealerCardNumber == 11:
        dealerCard = "Jack"
        dealerCardNumber = 10
      if dealerCardNumber == 12:
        dealerCard = "Queen"
        dealerCardNumber = 10
      if dealerCardNumber == 13:
        dealerCard = "King"
        dealerCardNumber = 10
      if dealerCardNumber == 14:
        dealerCard = "Ace"
        dealerCardNumber = 11
        
      dealerSum += dealerCardNumber

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
