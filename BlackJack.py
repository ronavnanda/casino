#Blackjack
import random

#set array of numbers to choose from
nums_array = [2,3,4,5,6,7,8,9,10,11,11,11,11,12,12,12,12,13,13,13,13,14]

#set playing to yes
playing = "Y"
busted = False

#game...
while playing.lower() == "y":

  #getting cards 1 and 2
  card1Rand = random.randint(0,21)
  card2Rand = random.randint(0,21)
  card1Num = nums_array[card1Rand]
  card2Num = nums_array[card2Rand]

  #making numbers to face value (ex: 11 --> Jack)
  if card1Num == 11:
    card1Value = "Jack"
  if card1Num == 12:
    card1Value = "Queen"
  if card1Num == 13:
    card1Value = "King"
  if card1Num == 14:
    card1Value = "Ace"

  #now for 2nd card
  if card2Num == 11:
    card2Value = "Jack"
  if card2Num == 12:
    card2Value = "Queen"
  if card2Num == 13:
    card2Value = "King"
  if card2Num == 14:
    card2Value = "Ace"

  #setting cards now to face value if neccessary
  card1 = str(card1Num)
  card2 = str(card2Num)
  if card1Rand>8: #8 cuz 2-10 is first 9 numbers.
    card1 = str(card1Value)
    card1Num = 10

  if card2Rand>8:
    card2 = str(card2Value)
    card2Num = 10

  playerSum = card1Num + card2Num

  #if total>21 and (card1Num == 1 or card2Num == 1): #this is implementation of ace, but can't work at this point so irrelevant here...
  #  total = total - 9;

  print(f"Your first card is {card1} and your second card is {card2}! Your total is {playerSum}.")

  hitting = input("Would you like to hit? (Y/N): ")

#dealing with improper inputs
  while hitting.lower() != "y" and hitting.lower() != "n":
    print("Invalid input. Please enter Y or N.")
    hitting = input("Would you like to hit?: ")

#output if not hitting
  if hitting.lower() == "n":
    print("You chose to stay")

#while hitting logic
  while hitting.lower() == "y":
    hitting = "n";
    print("You are hitting...")
    cardNum = nums_array[random.randint(0,21)]

    if cardNum == 11:
      cardName = "Jack"
    if cardNum == 12:
      cardName = "Queen"
    if cardNum == 13:
      cardName = "King"
    if cardNum == 14:
      cardName = "Ace"

    card = str(cardNum)
    if cardNum>8: #now we properly make cards Jack Queen King Ace
      card = str(cardName)
      cardNum = 10

    playerSum += cardNum

    print(f"Your card is {card}! Your total is {playerSum}.")

    if playerSum>21:
      print("You busted")
      busted = True;
    else:
      hitting = input("Would you like to hit? (Y/N): ")
  
  #dealer setup
  if(busted != True):
    print("Now it is time for the dealer!")
    dealerCard1Num = nums_array[random.randint(0,21)]
    dealerCard2Num = nums_array[random.randint(0,21)]
    
    cardName1 = str(dealerCard1Num)
    card1V = dealerCard1Num
    cardName2 = str(dealerCard2Num)
    card2V = dealerCard2Num
                    
    if dealerCard1Num == 11:
      cardName1 = "Jack"
      card1V = 10
    if dealerCard1Num == 12:
      cardName1 = "Queen"
      card1V = 10
    if dealerCard1Num == 13:
      cardName1 = "King"
      card1V = 10
    if dealerCard1Num == 14:
      cardName1 = "Ace"
      card1V = 10

    if dealerCard2Num == 11:
      cardName2 = "Jack"
      card2V = 10
    if dealerCard2Num == 12:
      cardName2 = "Queen"
      card2V = 10
    if dealerCard2Num == 13:
      cardName2 = "King"
      card2V = 10
    if dealerCard2Num == 14:
      cardName2 = "Ace"
      card2V = 10
  
    dealerSum = card1V + card2V

    if dealerSum > 16:
      print(f"Dealer has {cardName1} and {cardName2}, totaling to {dealerSum}. Dealer has to stand")
    while dealerSum<17:
      print(f"Dealer has {cardName1} and {cardName2}, totaling to {dealerSum}. Dealer has to hit")
      print("dealer is hitting...")
      dealerCardNum = nums_array[random.randint(0,21)]
      cardName = str(dealerCardNum)
      cardV = dealerCardNum
                    
      if dealerCardNum == 11:
        cardName = "Jack"
        cardV = 10
      if dealerCardNum == 12:
        cardName = "Queen"
        cardV = 10
      if dealerCardNum == 13:
        cardName = "King"
        cardV = 10
      if dealerCardNum == 14:
        cardName = "Ace"
        cardV = 10
        
      dealerSum += cardV
      print(f"Dealer got a {cardName}. Total sum is now {dealerSum}")
      if dealerSum > 21:
        print("Dealer busted")
  
    if(playerSum>dealerSum or dealerSum>21):
      print("You won!")
    elif(playerSum==dealerSum):
      print("It's a tie")
    else:
      print("You lost")
  playing = input("Would you like to continue playing? (Y/N): ")
