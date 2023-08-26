def print_board(board):
  #Prints the given board
  print("|-------------|")
  print("| Tic Tac Toe |")
  print("|-------------|")
  print("|             |")
  print("|    " + board[0][0] + " " + board[0][1] + " " + board[0][2] + "    |")
  print("|    " + board[1][0] + " " + board[1][1] + " " + board[1][2] + "    |")
  print("|    " + board[2][0] + " " + board[2][1] + " " + board[2][2] + "    |")
  print("|             |")
  print("|-------------|")
  print()

def select_space(board, move, turn):
  #Fills the space selected by the user or the Ai, in the given board 
  if move not in range(1,10):
    return False
  row = int((move-1)/3)
  col = (move-1)%3
  if board[row][col] != "X" and board[row][col] != "O":
    board[row][col] = turn
    return True
  else:
    return False

def available_moves(board):
  #Returns the available moves in the given board, will be usefull later in the minimax function
  moves = []
  for row in board:
    for col in row:
      if col != "X" and col != "O":
        moves.append(int(col))
  return moves

def has_won(board, player):
  #Returns True or False, if the given player has won the board
  for row in board:
    if row.count(player) == 3:
      return True
  for i in range(3):
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return True
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
      return True
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False
