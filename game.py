from tic_tac_toe import *

my_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]
# Editing the above board with "O" or "X" instead of any number, will change the starting board that AI is playing

print_board(my_board)
move = input("Enter a valid move from 1 to 9: \n")
symbol = input("Enter X or O as your symbol: \n")
select_space(my_board, int(move), symbol)
if symbol == "X":
   aisymbol = "O"
else:
   aisymbol = "X"

while not game_is_over(my_board):
   select_space(my_board, minimax(my_board, True)[1], aisymbol)
   print_board(my_board)
   if not game_is_over(my_board):
      move = input("Enter a valid move from : " + str(available_moves(my_board)) + ": \n")
      select_space(my_board, int(move), symbol)

if has_won(my_board, aisymbol):
   print("The AI won")
elif has_won(my_board, symbol):
   print("You won!")
else:
   print("It's a tie")