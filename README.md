# Snake-Water-Gun-game
The code is a simple implementation of the game "Snake, Water, Gun," which is a variation of the "Rock, Paper, Scissors" game. In this game, the user plays against the computer, and the winner is determined based on specific rules.
<br><br>
Importing the random module:<br>                       This module is used to generate random choices for the computer.<br><br>Printing options:<br>    print("Following are the options:- ")
print("Snake \nWater \nGun")           Prints the available options for the game.
<br><br>Creating a dictionary for choices:<br>dic = {1: "snake", 2: "water", 3: "gun"}<br>This dictionary maps integers to their corresponding string values.<br><br>Taking user input:<br>yrchoice = input("Enter your choice: ").lower()<br>This prompts the user to enter their choice and converts it to lowercase to ensure case insensitivity.<br><br>Generating computer's choice:<br>computer = random.choice([1, 2, 3])
comp = dic[computer]<br>This randomly selects an integer (1, 2, or 3) for the computer's choice and maps it to the corresponding string using the dictionary.
