#Blackjack
import random

nums_array = [2,3,4,5,6,7,8,9,10,11,11,11,11,12,12,12,12,13,13,13,13,1]

card1Rand = random.randint(0,21)
card2Rand = random.randint(0,21)
card1Num = nums_array[card1Rand]
card2Num = nums_array[card2Rand]

if card1Num == 11:
  card1V = "Jack (11)";
if card1Num == 12:
  card1V = "Queen (12)";
if card1Num == 13:
  card1V = "King (13)";
if card1Num == 1:
  card1V = "Ace (1 or 10)";

if card2Num == 11:
  card2V = "Jack (11)";
if card1Num == 12:
  card2V = "Queen (12)";
if card2Num == 13:
  card2V = "King (13)";
if card2Num == 1:
  card2V = "Ace (1 or 10)";

if card1Rand>8:
  card1 = str(card1V);

if card2Rand>8:
  card2 = str(card2V);

total = card1Num + card2Num;
if total>21 and (card1Num == 1 or card2Num == 1):
  total = total - 9;

print(f"Your first card is {card1} and your second card is {card2}! Your total is {total}.");

if total>21:
  print("You busted");

elif total<21:
  hitQ = input("Would you like to hit?(Y/N): ");
  while hitQ != "Y" and hitQ != "N":
    print("Invalid input. Please enter Y or N.");
    hitQ = input("Would you like to hit?(Y/N): ");
  if hitQ.upper() == "Y":
    cardThreeNum = nums_array[random.randint(0,21)]
    cardThree = str(cardThreeNum);
    total = total + cardThreeNum;
    print(f"Your third card is {cardThree}! Your total is {total}.");
    if total>21:
      print("You busted");

  else:
    print("You chose to stay");
