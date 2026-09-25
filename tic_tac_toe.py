import os

def create_board():
    """Creates a fresh, empty 3x3 board represented by a list of numbers."""
    return ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def display_board(board):
    """Prints the current state of the board grid to the screen."""
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal for a clean look
    print("\n--- Tic-Tac-Toe ---")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("-------------------")

def check_winner(board):
    """Checks all rows, columns, and diagonals for 3 matching marks."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for c in win_conditions:
        if board[c[0]] == board[c[1]] == board[c[2]]:
            print(board[c[0]])
            return True
    return False

def is_board_full(board):
    """Checks if there are any remaining empty numerical slots left."""
    for slot in board:
        if slot not in ["X", "O"]:
            return False
    return True

def play_game():
    """Main game loop managing turns, inputs, and state updates."""
    board = create_board()
    current_player = "X"
    game_over = False

    while not game_over:
        display_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Get and validate user input
        choice = input("Pick a slot (1-9): ").strip()
        
        if choice not in board or choice in ["X", "O"]:
            print("Invalid move! Slot is either taken or doesn't exist. Press Enter to try again...")
            input()
            continue
            
        # Update the board array directly
        board[int(choice) - 1] = current_player
        
        # Check game states
        if check_winner(board):
            print(check_winner(board))
            display_board(board)
            print(check_winner(board))
            print(f"🎉 Player {current_player} wins the game!")
            game_over = True
        elif is_board_full(board):
            display_board(board)
            print("🤝 It's a tie game!")
            game_over = True
        else:
            # Swap active player character
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
