from art import logo
from replit import clear
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  score=sum(cards)
  #represent Blackjack
  if (score==21 and len(cards)==2):
    return 0 
  elif 11 in cards :
    if score>21:
      cards.remove(11)
      cards.append(1)
  
  return score

def compare(user_score,computer_score):
  if user_score== computer_score:
    print("Draw")
  elif computer_score==0 :
    print("Lose, opponent has Blackjack ")
  elif user_score==0 :
    print("Win with a Blackjack")
  elif user_score>21 :
    print("You went over, You lose")
  elif computer_score>21 :
    print("Opponent went over. You win")
  elif computer_score>user_score :
    print("You lose ")
  else:
    print("You win")


def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())

  end=True
  while end:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")

    
    if user_score ==0 or computer_score==0 or user_score>21:
      end=False
    else:
      draw=input("Type 'y' to get another card, type 'n' to pass: ")
      if draw=="y":
          user_cards.append(deal_card())
      else:
          end=False
  
  while computer_score !=0 and computer_score<17 :
      computer_cards.append(deal_card())
      computer_score=calculate_score(computer_cards)
  print (f"Your Final cards is {user_cards} and Final score is {user_score} ")
  print (f"Computer Final cards is {computer_cards} and Final score is {computer_score} ")
  compare(user_score,computer_score)


while input("Do you want play a game of Blackjack? Type 'y' or 'n':" ).lower()=="y":
  clear()
  play_game()




