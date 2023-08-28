from tic_tac_toe import *

my_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]
# Editing the above board with "O" or "X" instead of any number, will change the starting board

def getvalidinput(my_board):
   # Gets valid input from the user for the next move
   while True:
      move = int(input("Enter a valid move from " + str(available_moves(my_board)) + " :" + "\n"))
      if move in available_moves(my_board):
         return move
      print("Wrong input, try again")

print_board(my_board)
while True:
   # Gets valid input of the user's symbol
   symbol = input("Enter X or O as your symbol: \n").upper()
   if symbol == "X" or symbol == "O":
      break
   print("Wrong input, try again")
select_space(my_board, getvalidinput(my_board), symbol)
if symbol == "X":
   aisymbol = "O"
else:
   aisymbol = "X"

while not game_is_over(my_board):
   # Inside the while loop, the AI plays its move first and then the user responds with the next available move
   select_space(my_board, minimax(my_board, True)[1], aisymbol)
   print_board(my_board)
   if not game_is_over(my_board):
      select_space(my_board, getvalidinput(my_board), symbol)

if has_won(my_board, aisymbol):
   print("The AI won")
elif has_won(my_board, symbol):
   print("You won!")
else:
   print("It's a tie")
