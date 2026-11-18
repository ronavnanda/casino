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
def deal_card(ace_count):
  cardValue = random.choice(nums_array) #get a value from the array
  if cardValue == 14:
    ace_count += 1
  card = card_names.get(cardValue, str(cardValue)) #this is .get() which looks for a key in the dictionary. str(cardValue) is returned when key isn't found
  cardValue = 10 if cardValue in (11,12,13) else 11 if cardValue == 14 else cardValue #compact way to write if/else logic
  return card, cardValue, ace_count

def determine_winner(player_sum, dealerSum):
  if player_sum>21:
    return "You busted"
  elif dealerSum>21:
    return "Dealer Busted, you win"
  elif player_sum>dealerSum:
    return "You win"
  elif player_sum==dealerSum:
    return "It's a tie"
  else:
    return "You lost"

def ace_management(ace_count, player_sum):
  while ace_count > 0 and player_sum > 21:
    player_sum -= 10
    ace_count -= 1
  return ace_count, player_sum

#set playing to yes
playing = "Y"

#game...
while playing.lower() == "y":

  ace_count = 0
  busted = False

  #getting cards 1 and 2
  card1, card1Number, ace_count = deal_card(ace_count)
  card2, card2Number, ace_count = deal_card(ace_count)

  player_sum = card1Number + card2Number

  ace_count, player_sum = ace_management(ace_count, player_sum)

  print(f"Your first card is {card1} and your second card is {card2}! Your total is {player_sum}.")

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

    card, cardNumber, ace_count = deal_card(ace_count)

    player_sum += cardNumber

    ace_count, player_sum = ace_management(ace_count, player_sum)

    print(f"Your card is {card}! Your total is now {player_sum}.")

    #determine if busted or not, determine if user will continue to hit.
    if player_sum>21:
      print("You busted")
      busted = True;
    elif player_sum==21:
      hitting = "n"
    else:
      hitting = input("Would you like to hit? (Y/N): ")

  #dealer setup
  if(busted != True):
    ace_count = 0
    print("Now it is time for the dealer!")
    dealerCard1, dealerCard1Value, ace_count = deal_card(ace_count)
    dealerCard2, dealerCard2Value, ace_count = deal_card(ace_count)

    dealerSum = dealerCard1Value + dealerCard2Value

    ace_count, dealerSum = ace_management(ace_count, dealerSum)


    if dealerSum > 16:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to stand")
    while dealerSum<17:
      print(f"Dealer has {dealerCard1} and {dealerCard2}, totaling to {dealerSum}. Dealer has to hit")
      print("dealer is hitting...")

      #get dealer their card
      dealerCard, dealerCardValue, ace_count = deal_card(ace_count)

      dealerSum += dealerCardValue

      ace_count, dealerSum = ace_management(ace_count, dealerSum)

      print(f"Dealer got a {dealerCard}. Total sum is now {dealerSum}")
      if dealerSum > 21:
        print("Dealer busted")

    print(determine_winner(player_sum, dealerSum))

  playing = input("Would you like to continue playing? (Y/N): ")
  while playing.upper() != "Y" and playing.upper() != "N":
    print("Invalid input. Please enter Y or N.")
    playing = input("Would you like to continue playing? (Y/N): ")
