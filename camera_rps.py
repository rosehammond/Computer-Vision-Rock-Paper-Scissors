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


    def __init__(self):
        #self.user_choice = user_choice
        #self.computer_choice = computer_choice
        self.user_wins = 0
        self.computer_wins = 0


    def countdown_timer(self):

        countdown_duration = 3
        start_time = None

        if start_time is None:
            start_time = time.time()

        remaining_time = countdown_duration - (time.time() - start_time)

        # Print the countdown timer
        if remaining_time > 0:
            print(f"Countdown: {int(remaining_time)} seconds", end='\r')
        

    def get_prediction(self):

        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        return prediction


    def convert_prediction_to_human_readable_prediction(self, prediction):
                                         
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
    
        game_choices = ["Rock", "Paper", "Scissors"]

        computer_choice = random.choice(game_choices)

        return computer_choice
    

    def get_winner(self, user_choice, computer_choice):

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

        while self.computer_wins < 3 and self.user_wins < 3:
            self.countdown_timer()
            prediction = self.get_prediction()
            user_choice = self.convert_prediction_to_human_readable_prediction(prediction)
            computer_choice = self.get_computer_choice()
            computer_wins, user_wins = self.get_winner(user_choice, computer_choice)

            if computer_wins == 3:
                print(f"The computer won {computer_wins} games to {user_wins}")
                
            elif user_wins == 3:
                print(f"You won {user_wins} games to {computer_wins}")
            
            # Press q to close the window
            elif cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows() 

    
    def __call__(self):
        self.play()


rock_paper_scissors_game = RockPaperScissors()
rock_paper_scissors_game()


"""
THis needs to go in the get prediction method
else:
            print(f"You chose:", end=" ")
            user_choice = get_prediction(prediction)
            break
            
        """

