import random

def get_computer_choice():
    
    game_choices = ["Rock", "Paper", "Scissors"]

    computer_choice = random.choice(game_choices)

    return computer_choice

def get_user_choice():

    while True:
        user_choice = input("Choose from Rock, Paper or Scissors: ").capitalize()

        if user_choice in ["Rock", "Paper", "Scissors"]:
            return user_choice
        else:
            print("Invalid choice. Choose from Rock, Paper or Scissors")
        
def get_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("You win!")

    else:
        print("You lose!")

def play():
    get_winner(get_user_choice(), get_computer_choice())

play()
