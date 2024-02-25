import random
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
def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
def minimax(board, depth, maximizing_player):
    if check_winner(board, "X"):
        return -10 + depth, None
    elif check_winner(board, "O"):
        return 10 - depth, None
    elif is_board_full(board):
        return 0, None
    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            eval, _ = minimax(board, depth + 1, False)
            board[i][j] = " "
            if eval > max_eval:
                max_eval = eval
                best_move = (i, j)
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            eval, _ = minimax(board, depth + 1, True)
            board[i][j] = " "
            if eval < min_eval:
                min_eval = eval
                best_move = (i, j)
        return min_eval, best_move
def get_ai_move(board):
    _, move = minimax(board, 0, True)
    return move
def get_player_move(board):
    while True:
        move = input("Enter your move (row column): ").split()
        if len(move) != 2:
            print("Invalid input. Please enter row and column separated by space.")
            continue
        try:
            row, col = map(int, move)
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Please enter an empty cell within the board range.")
        except ValueError:
            print("Invalid input. Please enter row and column as integers.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)
    print("Player", players[0], "goes first.")
    while True:
        player = players.pop(0)
        print_board(board)
        if player == "X":
            row, col = get_player_move(board)
        else:
            print("AI is making a move...")
            row, col = get_ai_move(board)
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"{player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

if _name_ == "_main_":
    play_game()
