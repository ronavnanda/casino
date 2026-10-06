#Blackjack
import random

#set array of numbers to choose from
nums_array = [2,3,4,5,6,7,8,9,10,11,11,11,11,12,12,12,12,13,13,13,13,14]

#set playing to yes
playing = "Y"

#game...
while playing.lower() == "y":

  #getting cards 1 and 2
  card1Rand = random.randint(0,21)
  card2Rand = random.randint(0,21)
  card1Num = nums_array[card1Rand]
  card2Num = nums_array[card2Rand]

  #making numbers to face value (ex: 11 --> Jack)
  if card1Num == 11:
    card1Value = "Jack";
  if card1Num == 12:
    card1Value = "Queen";
  if card1Num == 13:
    card1Value = "King";
  if card1Num == 14:
    card1Value = "Ace";

  #now for 2nd card
  if card2Num == 11:
    card2Value = "Jack";
  if card2Num == 12:
    card2Value = "Queen";
  if card2Num == 13:
    card2Value = "King";
  if card2Num == 14:
    card2Value = "Ace";

  #setting cards now to face value if neccessary
  card1 = str(card1Num);
  card2 = str(card2Num);
  if card1Rand>8: #8 cuz 2-10 is first 9 numbers.
    card1 = str(card1Value);
    card1Num = 10;

  if card2Rand>8:
    card2 = str(card2Value);
    card2Num = 10;

  total = card1Num + card2Num;

  #if total>21 and (card1Num == 1 or card2Num == 1): #this is implementation of ace, but can't work at this point so irrelevant here...
  #  total = total - 9;

  print(f"Your first card is {card1} and your second card is {card2}! Your total is {total}.");
  
  hitting = input("Would you like to hit? (Y/N): ");

#dealing with improper inputs
  while hitting.lower() != "y" and hitting.lower() != "n":
    print("Invalid input. Please enter Y or N.");
    hitting = input("Would you like to hit?: ");
  
#output if not hitting
  if hitting.lower() == "n":
    print("You chose to stay");

#while hitting logic
  while hitting.lower() == "y":
    hitting = "n";
    print("You are hitting...");
    cardNum = nums_array[random.randint(0,21)]

    if cardNum == 11:
      cardName = "Jack";
    if cardNum == 12:
      cardName = "Queen";
    if cardNum == 13:
      cardName = "King";
    if cardNum == 14:
      cardName = "Ace";

    card = str(cardNum);
    if cardNum>8: #now we properly make cards Jack Queen King Ace
      card = str(cardName);
      cardNum = 10;

    total += cardNum;

    print(f"Your card is {card}! Your total is {total}.");

    if total>21:
      print("You busted"); 
    else:
      hitting = input("Would you like to hit? (Y/N): ");
  
  playing = input("Would you like to continue playing? (Y/N): ")
