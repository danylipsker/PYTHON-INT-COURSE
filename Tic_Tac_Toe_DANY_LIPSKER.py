def welcome_message():
    clear_screen()
    print("\n********************************************************")
    print("* WELCOME TO PLAY TIC TAC TOE, CREATED By DANY LIPSKER *")
    print("********************************************************\n")


def userInput(name1="", symbol1="", name2="", symbol2=""):
    name1 = str(input("\nWhat is the FIRST player name please: \t"))
    name2 = str(input("\nWhat is the SECOND player name please: \t"))

    is_player_valid = False
    while not is_player_valid:
        symbol1 = str(input("choose among 'X' and 'O' only please !!! "))
        if symbol1 is "X":
            symbol2 = "O"
            is_player_valid = True
        elif symbol1 is "O":
            symbol2 = "X"
            is_player_valid = True
        else:
            print("Please enter X or O capital letters ONLY!")

    print()
    print(name1, "Thank you for choosing this :", symbol1)
    print(name2, "your symbol will be: ", symbol2)

    return name1, symbol1, name2, symbol2


def clear_screen():
    print("\n" * 100)


def initialize_board():
    ttt_board = [["-", "-", "-"],
                 ["-", "-", "-"],
                 ["-", "-", "-"]]
    return ttt_board


def display_board(board):
    print("\n")
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "     00 | 01 | 02")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "     10 | 11 | 12")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "     20 | 21 | 22")
    print("\n")


def input_coordinates():
    position_row = -1
    position_column = -1
    position_row, position_column = input("Enter a Row and a column in the range: 0-2: with a single space \t").split()
    while (position_row not in ["0", "1", "2"]) or (position_column not in ["0", "1", "2"]):
        print("You entered invalid values, please enter values between o to 2 ONLY...")
        position_row, position_column = input("Enter a Row and a column in the range: 0-2: with a single space  \t").split()

    return position_row, position_column

def check_if_position_available(board, row_int, col_int):
    if board[row_int][col_int] == "-":
        return True
    else:
        print("This position is already taken. Try again.")
        return False


def flip_player(current_player, current_player_name, player1_name, player2_name):
    if current_player == "X":
       current_player = "O"
    elif current_player == "O":
         current_player = "X"
    if current_player_name == player1_name:
       current_player_name = player2_name
    else:
       current_player_name = player1_name
    return current_player, current_player_name

def set_mark_in_board(set_X,set_Y,symbol,board):

    board[set_X][set_Y]=symbol
    return 0

def is_win(board):
    # Check if any of the rows have all the same value (and is not empty)
    row_0 = board[0][0] == board[0][1] == board[0][2] != "-"
    row_1 = board[1][0] == board[1][1] == board[1][2] != "-"
    row_2 = board[2][0] == board[2][1] == board[2][2] != "-"
    column_0 = board[0][0] == board[1][0] == board[2][0] != "-"
    column_1 = board[0][1] == board[1][1] == board[2][1] != "-"
    column_2 = board[0][2] == board[1][2] == board[2][2] != "-"
    diagonal_1 = board[0][0] == board[1][1] == board[2][2] != "-"
    diagonal_2 = board[0][2] == board[1][1] == board[2][0] != "-"
    if row_0 or row_1 or row_2 or column_0 or column_1 or column_2 or diagonal_1 or diagonal_2:
        return True
    else:
        return False

def is_tie(board):
    if "X" in board[0][:] and "O" in board[0][:]:
       row_0 = True
    else:
       row_0 = False

    if "X" in board[1][:] and "O" in board[1][:]:
       row_1 = True
    else:
       row_1 = False

    if "X" in board[2][:] and "O" in board[2][:]:
       row_2 = True
    else:
       row_2 = False

    if "X" in board[:][0] and "O" in board[:][0]:
       col_0 = True
    else:
       col_0 = False

    if "X" in board[:][1] and "O" in board[:][1]:
       col_1 = True
    else:
       col_1 = False

    if "X" in board[:][2] and "O" in board[:][2]:
       col_2 = True
    else:
       col_2 = False

    if ("X" in board[0][0] or "X" in board[1][1] or "X" in board[2][2]) and ("O" in board[0][0] or "O" in board[1][1] or "O" in board[2][2]):
        diag_1 = True
    else:
        diag_1 = False

    if ("X" in board[0][2] or "X" in board[1][1] or "X" in board[2][0]) and ("O" in board[0][2] or "O" in board[1][1] or "O" in board[2][0]):
        diag_2 = True
    else:
        diag_2 = False

    if row_0 and row_1 and row_2 and col_0 and col_1 and col_2 and diag_1 and diag_2:
        return True
    else:
        return False

def game_status(board):
    # Lets check for the game status
    # a) game running status
    # b) winner status
    # c) tie status
    if is_win(board):
       return "WIN"
    elif is_tie(board):
       return "TIE"
    else:
       return "RUNNING"

def play_tic_tac_toe():
    welcome_message()
    name1, symbol1, name2, symbol2 = userInput()
    board = initialize_board()
    display_board(board)
    current_game_status = "RUNNING"
    current_user = symbol1
    current_user_name = name1
    while current_game_status == "RUNNING":
          is_available = False
          while not is_available:
                print(f"{current_user_name}, now its your turn...")
                x, y = input_coordinates()
                is_available = check_if_position_available(board, int(x), int(y))
          set_mark_in_board(int(x), int(y), current_user, board)
          clear_screen()
          display_board(board)
          current_game_status = game_status(board)
          if current_game_status == "WIN":
             print(f"Congratulations {current_user_name} your mark is: {current_user}. You are the WINNER!!!")
             print("Game ENDS...")
             print()
          elif current_game_status == "TIE":
              print(f"GAME ENDS in TIE - NO WINNER, {name1} , {name2} can re-try!!!")
          current_user, current_user_name = flip_player(current_user, current_user_name, name1, name2)

def replay_game():
    your_choice = ""
    while your_choice != "Y" and your_choice != "N":
          your_choice = input("Do you want to play again? [Y/N]")
    if your_choice == "Y":
       return True
    elif your_choice == "N":
        return False

# ******************************************************************
# START of functions DEBUGGING
# ******************************************************************

# check V
# welcome_message()

# check V
# userInput()

# check V
# clear_screen()

# check V
# board = initialize_board()
# print(board)

# check V
# board = initialize_board()
# display_board(board)

# check V
# x, y = input_coordinates()
# print(f"X = {x} , Y = {y}")

# check V
# board = initialize_board()
# display_board(board)
# x, y = input_coordinates()
# is_available = check_if_position_available(board, int(x), int(y))
# print(f"The position in board of X = {x} , Y = {y} is available: {is_available}")

# check V
# board = initialize_board()
# display_board(board)
# x, y = input_coordinates()
# is_available = check_if_position_available(board, int(x), int(y))
# print(f"The position in board of X = {x} , Y = {y} is available: {is_available}")
# symbol = 'X'
# if is_available:
#    set_mark_in_board(int(x), int(y), symbol, board)
# display_board(board)

# check V
# current_player = 'X'
# flip_player(current_player)
# print(current_player)
# current_player = 'O'
# flip_player(current_player)
# print(current_player)


# check V
# board = [["X", "O", "X"],
#          ["O", "X", "O"],
#          ["-", "-", "X"]]
# display_board(board)
# current_game_status = game_status(board)
# print(f"This game status is: {current_game_status}")
#
# board = [["O", "O", "X"],
#          ["O", "X", "O"],
#          ["O", "X", "X"]]
# display_board(board)
# current_game_status = game_status(board)
# print(f"This game status is: {current_game_status}")
#
# board = [["O", "O", "X"],
#          ["X", "X", "O"],
#          ["O", "-", "X"]]
# display_board(board)
# current_game_status = game_status(board)
# print(f"This game status is: {current_game_status}")
#
# board = [["-", "O", "X"],
#          ["X", "-", "O"],
#          ["O", "-", "X"]]
# display_board(board)
# current_game_status = game_status(board)
# print(f"This game status is: {current_game_status}")

# check V
play_game = True
while play_game:
      play_tic_tac_toe()
      play_game = replay_game()

# ******************************************************************
# END of functions DEBUGGING
# ******************************************************************
