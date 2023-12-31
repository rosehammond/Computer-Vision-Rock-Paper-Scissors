# Computer-Vision-Rock-Paper-Scissors


## Table of Contents

- Description
- Technologies utilised
- Installation instructions
- Usage instructions
- File structure of the project
- Code structure
- License information


## Description

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock.

The player who shows the first option that beats the other player's option wins that round.

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera. The game is won when either the user or the computer wins 3 rounds.

Also included is a version where the user can play manually against the computer in the terminal, without the need for a camera.

In this project, I consolidated my learning in basic Python methods including while loops, if-else statements, creating functions, and using object-oriented programming.
I also experimented with some new technology - "Teachable Machine", and learned about NumPy arrays.


## Technologies utilised

- Python
- Teachable Machine

  
## Installation instructions

1. Clone the repository to your local machine: git clone https://github.com/rosehammond/computer-vision-rock-paper-scissors.git
2. Navigate to the project directory in your terminal
3. To run the interactive camera version use the following command: *python camera_rps.py*


## Usage instructions

1. The terminal will display a 3-second countdown timer, during this time the user should hold up a hand signal of either rock, paper, or scissors.
2. The camera will open and record this hand signal.
3. The terminal will display, in text, what hand signal the user chose.
4. The terminal will then display the computer choice and who won that round.
5. The camera will close.
6. The game will pause for 5 seconds, then a new timer will begin for round 2.
7. The first player to win 3 rounds, wins the game and this will be announced in the terminal.


## File structure of the project

- **camera_rps.py** contains the Python code for this game.
- **keras_model.h5** created using Teachable Machine to predict what hand signal the user is holding up
- **labels.txt** labels for the different hand signals
- **requirements.txt** all the dependencies for the game, can be installed using the command *pip install -r requirements.txt*


## Code Structure

- ``` RockPaperScissors(): ``` Class which includes all the attributes and methods for the game
- ``` countown_timer(): ``` Method to display a 3-second countdown timer
- ``` get_prediction(): ``` Method to open the camera and take a frame of the user's hand signal
- ``` convert_prediction_to_human_readable_prediction(prediction): ``` Method to convert the frame image into text
- ``` get_computer_choice(): ``` Method to allow the computer to randomly select an option
- ``` get_winner(user_choice, computer_choice): ``` Method to compare the user choice to the computer choice, display the winner, and add 1 point to either the user or computer (or no points if it is a tie) 
- ``` play(): ``` Method to code the logic of the game, allowing the game to play more rounds until either the user or computer wins 3 times. The overall winner is then revealed.


## License information

This project is licensed under the MIT License - see the LICENSE.txt file for details.
