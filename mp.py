
board = [" " for _ in range(9)]


def display_board():
    """Display the current state of the board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def player_input(player):
    """
    Ask the player for a position (1–9) and update the board.
    Ensures the input is valid and the position is empty.
    """
    while True:
        try:
            position = int(input(f"Player {player}, choose a position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Please choose a number between 1 and 9.")
            elif board[position] != " ":
                print("That position is already taken. Try again.")
            else:
                board[position] = player
                break

        except ValueError:
            print("Invalid input. Please enter a number.")


def check_win():
    """Check if there is a winner."""
    win_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    return None


def check_tie():
    """Check if the board is full (tie)."""
    return " " not in board


def play():
    """Main game loop."""
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    display_board()

    while True:
        player_input(current_player)
        display_board()

        winner = check_win()
        if winner:
            print(f"🎉 Player {winner} wins!")
            break

        if check_tie():
            print("It's a tie! 🤝")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


play()
