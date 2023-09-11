import time
import random
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
class_names = open("labels.txt", "r").readlines()


class RockPaperScissors:
    """
    This class lets a user play rock-paper-scissors against the computer.
    
    Attributes:
        user_wins (int): how many rounds the user has won during the game, defaults to 0.
        computer_wins (int): how many rounds the computer has won during the game, defaults to 0.
    """
    def __init__(self):
        """
        See help(RockPaperScissors) for accurate signature.
        """
        self.user_wins = 0
        self.computer_wins = 0

    def countdown_timer(self):
        """
        This method displays a 3-second countdown timer in the terminal. 

        The purpose of this functions is to countdown from 3 to 0.
        """
        countdown_duration = 3

        for remaining_time in range(countdown_duration, 0, -1):
            print(f"Countdown: {remaining_time} seconds", end='\r')
            time.sleep(1)  # Pause for 1 second

        print("Countdown: 0 seconds")

    def get_prediction(self):
        """
        This method opens the camera and captures the hand gesture from the user. 

        The purpose of this functions is to capture the image and return it as a NumPy array.
        """
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        return prediction

    def convert_prediction_to_human_readable_prediction(self, prediction):
        """
        This method converts the captured image prediction into a readable output.

        Args:
            prediction (ndarray): the prediction as a NumPy array.

        The purpose of this method is to find the index of the highest value in the NumPy array. 
        It then checks if the index is: 0, 1, 2, or 3.
        Each of these indices relate to a different output: Rock, Paper, Scissors, or Nothing.
        The method then assigns this value as the user_choice variable and returns it.
        """
        # Returns the index of the highest value in the NumPy array                                 
        max_index = np.argmax(prediction) 

        if max_index == 0:
            print("You chose: Rock")
            user_choice = "Rock"
        elif max_index == 1:
            print("You chose: Paper")
            user_choice = "Paper"
        elif max_index == 2:
            print("You chose: Scissors")
            user_choice = "Scissors"
        else: 
            print("You chose: Nothing")
            user_choice = "Nothing"
        
        return user_choice

    def get_computer_choice(self):
        """
        This method allows the computer to make a random choice: Rock, Paper, or Scissors. 

        The purpose of this functions is to assign this choice as the variable 
        computer_choice and return it.
        """
        game_choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(game_choices)
        return computer_choice
    
    def get_winner(self, user_choice, computer_choice):
        """
        This method compares the user choice to the computer choice.

        Args:
            user_choice (str): the choice of the user.
            computer_choice (str): the choice of the computer.

        The purpose of this method is to use the comparison of the user choice and computer choice
        to return who wins and increase their score by 1.
        No scores will increase if it is a tie.
        """
        if user_choice == computer_choice:
            print(f"It's a tie! Computer chose {computer_choice}")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            print(f"You win! Computer chose {computer_choice}")
            self.user_wins += 1 
        else:
            print(f"You lose! Computer chose {computer_choice}")
            self.computer_wins += 1

        return self.computer_wins, self.user_wins

    def play(self):
        """
        This method allows the game to be played until one player wins 3 rounds. 

        The purpose of this method is to close and reopen the camera between rounds.
        This method also calls the other methods from the class in order to continue the loop.
        The loop will be broken and the game ends when either the user or computer wins 3 times.
        """
        global cap
        while self.computer_wins < 3 and self.user_wins < 3:
            self.countdown_timer()
            cap = cv2.VideoCapture(0) # Open the camera
            prediction = self.get_prediction()
            user_choice = self.convert_prediction_to_human_readable_prediction(prediction)
            computer_choice = self.get_computer_choice()
            computer_wins, user_wins = self.get_winner(user_choice, computer_choice)
            
            cv2.waitKey(1)  # Update the OpenCV window
            cap.release()
            cv2.destroyAllWindows()

            # Press q to close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif computer_wins == 3:
                print(f"The computer won {computer_wins} games to {user_wins}")
            elif user_wins == 3:
                print(f"You won {user_wins} games to {computer_wins}")
            elif computer_wins > user_wins:
                print(f"The computer is winning by {computer_wins} games to {user_wins}")
                print("Next round will start in 5 seconds.")
                time.sleep(5)
            elif user_wins > computer_wins:
                print(f"You are winning by {user_wins} games to {computer_wins}")
                print("Next round will start in 5 seconds.")
                time.sleep(5)
            else:
                print(f"It's currently a draw {user_wins} - {computer_wins}.")
                print("Next round will start in 5 seconds.")
                time.sleep(5)
            
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows() 

    def __call__(self):
        self.play()


if __name__ == '__main__':
    rock_paper_scissors_game = RockPaperScissors()
    rock_paper_scissors_game()