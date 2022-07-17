from art import logo
import random
from replit import clear

my_guess=random.choice(range(1,101))

def user_guess(my_guess, difficulty_level):

  if difficulty_level=='easy':
    attempts_remaining=10
  elif difficulty_level=='hard':
    attempts_remaining=5
  
  is_game_cont=True

  while is_game_cont:

    print(f"You have {attempts_remaining} attempts remaining.")
  
    if attempts_remaining==0:
      print("You've run out guesses. You lose.")
      is_game_cont=False
      return is_game_cont

    user_guess=int(input("Make a guess: "))

    if user_guess==my_guess:
      is_game_cont=False
      print(f" You got it. The answer is: {my_guess}")
      return is_game_cont
    elif user_guess!=my_guess:
      attempts_remaining-=1
      if user_guess>my_guess:
        print("Too high!")
      elif user_guess<my_guess:
        print("Too low!")     
  is_game_cont=False
      
def play_game():
  
  print(logo)
  print("Welcome to the number guessing name! ")
  print("I'm thinking of a number between 1 and 100. ")
  level=input("Choose a difficulty tpe 'easy' or 'hard': ").lower()

  user_guess(level)  

  play_again=input("Do you want to play again? Type 'y' or 'n': ")
  while play_again=='y':
    clear()
    play_game()

play_game()




