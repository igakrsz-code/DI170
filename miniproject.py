# -----------------------------
# Step 1: Create the game board
# -----------------------------

def create_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]


# -----------------------------
# Step 2: Display the board
# -----------------------------

def display_board(board):
    print("\n")
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("---+---+---")
    print("\n")


# -----------------------------
# Step 3: Get player input
# -----------------------------

def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("❌ Invalid position. Choose numbers between 1 and 3.")
            elif board[row][col] != " ":
                print("❌ That spot is already taken. Try again.")
            else:
                return row, col

        except ValueError:
            print("❌ Please enter numbers only.")


# -----------------------------
# Step 4: Check for a win
# -----------------------------

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# -----------------------------
# Step 5: Check for a tie
# -----------------------------

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


# -----------------------------
# Step 6: Main game loop
# -----------------------------

def play():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)

        row, col = player_input(board, current_player)
        board[row][col] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("🤝 It's a tie!")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# -----------------------------
# Start the game
# -----------------------------

play()
