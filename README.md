# Computer-Vision-Rock-Paper-Scissors

## Table of Contents

- Installation instructions
- Usage instructions
- File structure
- License information


## A description of the project: what it does, the aim of the project, and what you learned

Rock-Paper-Scissors is a game in which each player simultaneously shows one of three hand signals representing rock, paper, or scissors. Rock beats scissors. Scissors beats paper. Paper beats rock.

The player who shows the first option that beats the other player's option wins.

This is an implementation of an interactive Rock-Paper-Scissors game, in which the user can play with the computer using the camera.

Also included is a version where the user can play manually against the computer in the terminal, without the need for a camera.

In this project, I consolidated my learning in basic Python methods (while loops, if-else statements, creating functions)
I also learned some new technology: "Teachable Machine"...


## Installation instructions

1. Clone the repository to your local machine: git clone https://github.com/rosehammond/computer-vision-rock-paper-scissors.git
2. Navigate to the project directory
3. Run the game: python _______________


## Usage instructions

## File structure of the project

### Manual version
The game consists of three main functions:

get_computer_choice()
This function randomly selects the computer's choice from Rock, Paper, or Scissors.

get_user_choice()
This function prompts the user to input their choice and validates that the input is one of the valid choices (Rock, Paper, or Scissors).

get_winner(user_choice, computer_choice)
This function determines the winner based on the choices made by the user and the computer. It checks for ties and winning conditions.

play()
The play() function orchestrates the entire game by calling the above functions and displaying the outcome.

### Interactive version


## License information

This project is licensed under the MIT License - see the LICENSE.txt file for details.
