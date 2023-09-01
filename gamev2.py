import tkinter
from tkinter import *
import customtkinter
from tic_tac_toe import *

def nextstep(board):
    # This function will be called each time after the user's turn
    move = minimax(board, True)[1]
    select_space(board, move , "O")
    print_board(board)
    # The following part needs optimizing
    if move == 1:
        update1("O", board, move)
    elif move == 2:
        update2("O", board, move)
    elif move == 3:
        update3("O", board, move)
    elif move == 4:
        update4("O", board, move)
    elif move == 5:
        update5("O", board, move)
    elif move == 6:
        update6("O", board, move)
    elif move == 7:
        update7("O", board, move)
    elif move == 8:
        update8("O", board, move)
    elif move == 9:
        update9("O", board, move)

# The functions updateX will update the text variable of each button, whether the user or the AI presses it
def update1(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field1.set(symbol)
    select_space(board, move, symbol)
    print_board(board)
    nextstep(board)

def update2(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field2.set(symbol)
    select_space(board, move, symbol)

def update3(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field3.set(symbol)
    select_space(board, move, symbol)

def update4(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field4.set(symbol)
    select_space(board, move, symbol)

def update5(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field5.set(symbol)
    select_space(board, move, symbol)

def update6(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field6.set(symbol)
    select_space(board, move, symbol)

def update7(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field7.set(symbol)
    select_space(board, move, symbol)

def update8(symbol, board, move):
    global expression
    expression = expression + str(symbol)
    expression_field8.set(symbol)
    select_space(board, move, symbol)

def update9(symbol, my_board, move):
    global expression
    expression = expression + str(symbol)
    expression_field9.set(symbol)
    select_space(my_board, move, symbol)

my_board = [
	["1", "2", "3"],
	["4", "5", "6"],
	["7", "8", "9"]
]

# Window settings and frame settings
customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry('800x600')
root.resizable(False, False)
root.title("Tic Tac Toe Game v2")
root.iconbitmap(default="icon2.ico")

menu_frame = Frame(root, width= 200, height=600, bd = 0, highlightbackground= "black",bg = "#2c69a5", highlightcolor= "black", highlightthickness= 1)
menu_frame.pack(side=LEFT)

game_frame = Frame(root, width=500, height=500, bg="grey")
game_frame.pack(expand=True)

expression = ""
expression_field1 = StringVar()
expression_field2 = StringVar()
expression_field3 = StringVar()
expression_field4 = StringVar()
expression_field5 = StringVar()
expression_field6 = StringVar()
expression_field7 = StringVar()
expression_field8 = StringVar()
expression_field9 = StringVar()
symbol = "X"


one_button = Button(game_frame, textvariable = expression_field1, fg= "black", width= 12, height= 6, bd= 0, bg= "#eee", cursor = "hand2", command = lambda: update1(symbol, my_board, 1)).grid(row = 0, column = 0, padx = 1, pady = 1)
two_button = Button(game_frame, textvariable = expression_field2, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update2(symbol, my_board, 2)).grid(row = 0, column = 1, padx = 1, pady = 1)
three_button = Button(game_frame, textvariable = expression_field3, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update3(symbol, my_board, 3)).grid(row = 0, column = 2, padx = 1, pady = 1)
four_button = Button(game_frame, textvariable = expression_field4, fg= "black", width= 12, height= 6, bd= 0, bg= "#eee", cursor = "hand2", command = lambda: update4(symbol, my_board, 4)).grid(row = 1, column = 0, padx = 1, pady = 1)
five_button = Button(game_frame, textvariable = expression_field5, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update5(symbol, my_board, 5)).grid(row = 1, column = 1, padx = 1, pady = 1)
six_button = Button(game_frame, textvariable = expression_field6, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update6(symbol, my_board, 6)).grid(row = 1, column = 2, padx = 1, pady = 1)
seven_button = Button(game_frame, textvariable = expression_field7, fg= "black", width= 12, height= 6, bd= 0, bg= "#eee", cursor = "hand2", command = lambda: update7(symbol, my_board, 7)).grid(row = 2, column = 0, padx = 1, pady = 1)
eight_button = Button(game_frame, textvariable = expression_field8, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update8(symbol, my_board, 8)).grid(row = 2, column = 1, padx = 1, pady = 1)
nine_button = Button(game_frame, textvariable = expression_field9, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update9(symbol, my_board, 9)).grid(row = 2, column = 2, padx = 1, pady = 1)

root.mainloop()


