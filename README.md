# Snake-Water-Gun-game
Thi PYTHON code is a simple implementation of the game "Snake, Water, Gun," which is a variation of the "Rock, Paper, Scissors" game. In this game, the user plays against the computer, and the winner is determined based on specific rules.
<br><br>
Importing the random module:<br> import random<br>                      This module is used to generate random choices for the computer.<br><br>Printing options:<br>    print("Following are the options:- ")<br>
print("Snake \nWater \nGun") <br>          Prints the available options for the game.
<br><br>Creating a dictionary for choices:<br>dic = {1: "snake", 2: "water", 3: "gun"}<br>This dictionary maps integers to their corresponding string values.<br><br>Taking user input:<br>yrchoice = input("Enter your choice: ").lower()<br>This prompts the user to enter their choice and converts it to lowercase to ensure case insensitivity.<br><br>Generating computer's choice:<br>computer = random.choice([1, 2, 3])<br>
comp = dic[computer]<br>This randomly selects an integer (1, 2, or 3) for the computer's choice and maps it to the corresponding string using the dictionary.<br><br>Determining the result:<br>This block of code determines the result of the game based on the user's choice and the computer's choice.<br>
The if statement checks if both choices are the same, resulting in a draw.<br><br>
The elif statements check all other combinations to determine the winner based on the rules of the game:<br>
Snake drinks water (Snake wins)<br>
Snake is killed by gun (Gun wins)<br>
Water drowns gun (Water wins)<br>
