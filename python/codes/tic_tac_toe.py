import random

def print_board(board):
    i = 0
    while i < 3:
        print("|", end=' ')
        j = 0
        while j < 3:
            print(board[i][j], end=' | ')
            j += 1
        print()
        print("-" * 13)
        i += 1

def check_victory(board, player):
    i = 0
    while i < 3:
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player:
            return True

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            return True
        
        i += 1

    return False

def cpu_move(board):
    available_moves = []
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if board[i][j] == " ":
                available_moves.append((i, j))
            j += 1
        i += 1
    print()

    return random.choice(available_moves)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    vs_cpu = input("Do you want to play against the CPU? (yes/no): ").lower() == "yes"

    players = ["O", "X"]
    current_player_index = 0

    board = []
    i = 0
    while i < 3:
        row = []
        j = 0
        while j < 3:
            row.append(" ")
            j += 1
        board.append(row)
        i += 1

    moves = 0
    running = True
    while running:
        print_board(board)

        # Ask for player's move
        valid_move = True
        while valid_move:
            if vs_cpu and current_player_index == 0:
                row, col = cpu_move(board)
            else:
                row = int(input(f"{players[current_player_index]}, enter the row (1, 2, or 3): ")) - 1
                col = int(input(f"{players[current_player_index]}, enter the column (1, 2, or 3): ")) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                valid_move = False
            else:
                print("Invalid move. Try again.")

        # Update the board
        board[row][col] = players[current_player_index]
        moves += 1

        # Check for victory
        if check_victory(board, players[current_player_index]):
            print_board(board)
            print(f"{players[current_player_index]} wins!")
            break

        # Check for a draw
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player_index = 1 - current_player_index

if __name__ == "__main__":
    tic_tac_toe()
