## **Battleship Game**

### **Overview**
This is a Python implementation of the classic Battleship game, developed as part of the CSC108/CSCA08 course at the University of Toronto for the Winter 2024 term.

The game involves two players, each with a fleet of ships placed on a grid. Players take turns guessing the coordinates of their opponent's ships to sink them. The first player to sink all of their opponent's ships wins the game.

### **Game Rules**
**Grid Setup:** Each player has a grid on which they place their ships. Ships cannot overlap and must be placed either horizontally or vertically.

**Turns:** Players take turns guessing the coordinates of their opponent's ships.

**Hits and Misses:** If a player guesses a coordinate occupied by an opponent's ship, it's a hit. Otherwise, it's a miss.

**Winning:** The game ends when one player has sunk all of their opponent's ships.

### **Implementation Details**
The game is implemented in Python and consists of the following modules:

- **battleship_game_functions.py:** Contains functions implementing the core logic of the game, such as grid setup, turn handling, and win conditions.

- **play_battleship_game.py:** Provides a user interface for playing the game. It interacts with the functions defined in battleship_game_functions.py to execute the game logic.

### **Usage**
To play the game, simply run play_battleship_game.py from the command line. Follow the prompts to set up your fleet and start playing.
