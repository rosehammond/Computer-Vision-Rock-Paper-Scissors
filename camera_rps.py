# Create a new function called get_prediction that will return the output of the model you used earlier.

# Remember that the output of the model you downloaded is a list of probabilities for each class. 
# You need to pick the class with the highest probability. So, for example, assuming you trained the 
# model in this order: "Rock", "Paper", "Scissors", and "Nothing", if the first element of the list is 0.8, 
# the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model 
# predicts that you showed "Rock" to the camera with a confidence of 0.8.

# The model can make many predictions at once if given many images. 
# In your case you only give it one image at a time. 
# That means that the first element in the list returned from the model is a list of probabilities 
# for the four different classes. Print the response of the model if you are unclear of this.
import time
import random
import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
class_names = open("labels.txt", "r").readlines()


def get_computer_choice():
    
    game_choices = ["Rock", "Paper", "Scissors"]

    random_computer_choice = random.choice(game_choices)

    return random_computer_choice

def get_prediction(input_data):

    max_index = np.argmax(input_data)

    if max_index == 0:
        print("Rock")
        return "Rock"
    elif max_index == 1:
        print("Paper")
        return "Paper"
    elif max_index == 2:
        print("Scissors")
        return "Scissors"
    else: 
        print("Nothing")
        return "Nothing"


countdown_duration = 3  # Set the countdown duration in seconds
start_time = None

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    
    if start_time is None:
        start_time = time.time()

    remaining_time = countdown_duration - (time.time() - start_time)

    # Print the countdown timer
    if remaining_time > 0:
        print(f"Countdown: {int(remaining_time)} seconds", end='\r')
    else:
        print(f"You chose:", end=" ")
        user_choice = get_prediction(prediction)
        break
    
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

computer_choice = get_computer_choice()
computer_wins = 0
user_wins = 0

def get_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        print(f"It's a tie! Computer chose {computer_choice}")

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print(f"You win! Computer chose {computer_choice}")
        user_wins += 1 

    else:
        print(f"You lose! Computer chose {computer_choice}")
        computer_wins += 1
        
    return computer_wins, user_wins

def play(): 

    if computer_wins < 3 and user_wins < 3:
        get_prediction(prediction)
        get_computer_choice()
        get_winner(user_choice, computer_choice)

    elif computer_wins == 3:
        print(f"The computer won {computer_wins} games to {user_wins}")
        
    elif user_wins == 3:
        print(f"You won {user_wins} games to {computer_wins}")
            
play()

# The game should be repeated until either the computer or the user wins three rounds.

# Feel free to code the logic as you want, but make sure you defined at least two variables to keep track 
# of the score of the computer and the user. Name them computer_wins and user_wins respectively.

# Quick tip here: You shouln't use a while loop inside the main while loop 
# (the one capturing and showing your image). 
# The reason behind it is that, when you are inside the nested loop, 
# the code in the main while loop won't run, and hence, the camera won't show anything.