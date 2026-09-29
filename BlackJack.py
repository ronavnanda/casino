#Blackjack
import random

nums_array = [1,2,3,4,5,6,7,8,9,10,11,11,11,11,12,12,12,12,13,13,13,13]
suits_array = ["Hearts", "Diamonds", "Clubs", "Spades"]

cardOne = nums_array[random.randint(0,21)]
cardTwo = nums_array[random.randint(0,21)]

print(f"Your first card is {cardOne} and your second card is {cardTwo}! Your total is {cardOne+cardTwo}.");
if (cardOne+cardTwo) >21:
  print("You busted")
