def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move():
    while True:
        move = input("Enter your move (row column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter row and column separated by space.")
            continue
        try:
            row, col = map(int, move)
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter row and column as integers.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        row, col = get_move()
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            turn += 1
        else:
            print("That cell is already occupied. Try again.")

if _name_ == "_main_":
    play_game()
