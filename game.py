
import streamlit as st
import numpy as np

# Initialize the game
def initialize_game():
    return np.full((3, 3), ''), 'human'  # Create a 3x3 board and set starting player

# Check for a win
def check_winner(board):
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] != '':
            return board[i, 0]
        if board[0, i] == board[1, i] == board[2, i] != '':
            return board[0, i]
    if board[0, 0] == board[1, 1] == board[2, 2] != '':
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] != '':
        return board[0, 2]
    return None

# Check if the board is full (draw)
def is_draw(board):
    return '' not in board

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'AI':
        return 10 - depth
    elif winner == 'human':
        return depth - 10
    elif is_draw(board):
        return 0
    
    if is_maximizing:
        max_eval = -np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == '':
                    board[i, j] = 'AI'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i, j] = ''
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = np.inf
        for i in range(3):
            for j in range(3):
                if board[i, j] == '':
                    board[i, j] = 'human'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i, j] = ''
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI move function using minimax
def ai_move(board):
    best_score = -np.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i, j] == '':
                board[i, j] = 'AI'
                score = minimax(board, 0, False, -np.inf, np.inf)
                board[i, j] = ''
                if score > best_score:
                    best_score = score
                    move = (i, j)
    board[move[0], move[1]] = 'AI'

# Display the game board with buttons
def display_board(board):
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                button_key = f'button_{i}_{j}_{st.session_state.turn}'  # Unique key for each button
                if st.button(board[i, j] if board[i, j] else '', key=button_key):
                    return i, j
    return None, None

# Main function for the app
def main():
    if 'board' not in st.session_state:
        st.session_state.board, st.session_state.current_player = initialize_game()
        st.session_state.game_over = False
        st.session_state.turn = 0

    st.title("Tic-Tac-Toe: Human vs AI")
    board = st.session_state.board
    current_player = st.session_state.current_player
    game_over = st.session_state.game_over

    if not game_over:
        if current_player == 'human':
            # Get player's move
            i, j = display_board(board)
            if i is not None and j is not None and board[i, j] == '':
                board[i, j] = 'human'
                winner = check_winner(board)
                if winner:
                    st.success(f"Player {winner} wins!")
                    st.balloons()
                    game_over = True
                    st.session_state.game_over = True
                elif is_draw(board):
                    st.warning("It's a draw!")
                    game_over = True
                    st.session_state.game_over = True
                else:
                    current_player = 'AI'
                    st.session_state.current_player = current_player

        if current_player == 'AI' and not game_over:
            # AI makes its move
            ai_move(board)
            winner = check_winner(board)
            if winner:
                st.write(f"Player {winner} wins!") 
                game_over = True
                st.session_state.game_over = True
            elif is_draw(board):
                st.warning("It's a draw!")
                game_over = True

                st.session_state.game_over = True
            else:
                current_player = 'human'
                st.session_state.current_player = current_player

            # Update session state
            st.session_state.board = board

    if st.button("Restart Game"):
        st.session_state.board, st.session_state.current_player = initialize_game()
        st.session_state.game_over = False
        st.session_state.turn += 1  # Increment turn to ensure unique keys

if __name__ == "__main__":
    main()



