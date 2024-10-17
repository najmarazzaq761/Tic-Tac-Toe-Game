# Tic-Tac-Toe: Human vs AI

## Overview
This is a **Tic-Tac-Toe** game where a human player competes against a smart AI opponent. The AI utilizes the **minimax algorithm with alpha-beta pruning** to make optimal moves, making it a challenging game for the player. The game is built with **Python** and the **Streamlit** library for an interactive UI.

## Features
- Play Tic-Tac-Toe against an AI that makes intelligent moves.
- The AI uses minimax with alpha-beta pruning to optimize its strategy.
- Clear indication of game status: player win, AI win, or a draw.
- Restart the game anytime to play again.
- Clean and simple interface powered by Streamlit.

## Technologies Used
- **Python**: Game logic and AI implementation.
- **NumPy**: To handle the game board as a 2D array.
- **Minimax Algorithm**: AI logic with alpha-beta pruning for efficiency.
- **Streamlit**: For building the interactive web app UI.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/najmarazzaq761/tic-tac-toe-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tic-tac-toe-game
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run game.py
   ```

## How to Play
1. The game starts with the human player making the first move as **X**.
2. The AI plays as **O** and tries to block and win using the minimax algorithm.
3. The game ends when there is a winner or a draw. Click **Restart Game** to play again!

## Demo


https://github.com/user-attachments/assets/fc97b90f-7825-439a-9b1d-16ec192ae980


## Future Improvements
- Add difficulty levels to adjust the AI's intelligence.
- Implement a two-player mode.
- Improve UI with additional design elements.

## Contributing
Feel free to fork the repository and submit pull requests. Any suggestions and improvements are welcome!

## License
This project is licensed under the MIT License.
