import tkinter
from tkinter import *
import customtkinter
from tic_tac_toe import *


def nextstep(board):
    # This function will be called each time after the user's turn
    global turn
    if turn == "AI":
        turn = "Player"
        move = minimax(board, True)[1]
        select_space(board, move, "O")
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
    else:
        turn = "AI"

    if game_is_over(board):
        # This part will disable the buttons, when the game is over
        one_button.configure(state="disabled", bg="#bcbcbc")
        two_button.configure(state="disabled", bg="#bcbcbc")
        three_button.configure(state="disabled", bg="#bcbcbc")
        four_button.configure(state="disabled", bg="#bcbcbc")
        five_button.configure(state="disabled", bg="#bcbcbc")
        six_button.configure(state="disabled", bg="#bcbcbc")
        seven_button.configure(state="disabled", bg="#bcbcbc")
        eight_button.configure(state="disabled", bg="#bcbcbc")
        nine_button.configure(state="disabled", bg="#bcbcbc")


# The functions updateX will update the text variable of each button, whether the user or the AI presses it
def update1(symbol, board, move):
    expression_field1.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    one_button.configure(state="disabled")


def update2(symbol, board, move):
    expression_field2.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    two_button.configure(state="disabled")


def update3(symbol, board, move):
    expression_field3.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    three_button.configure(state="disabled")


def update4(symbol, board, move):
    expression_field4.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    four_button.configure(state="disabled")


def update5(symbol, board, move):
    expression_field5.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    five_button.configure(state="disabled")


def update6(symbol, board, move):
    expression_field6.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    six_button.configure(state="disabled")


def update7(symbol, board, move):
    expression_field7.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    seven_button.configure(state="disabled")


def update8(symbol, board, move):
    expression_field8.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    eight_button.configure(state="disabled")


def update9(symbol, board, move):
    expression_field9.set(symbol)
    select_space(board, move, symbol)
    nextstep(board)
    nine_button.configure(state="disabled")


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

menu_frame = Frame(root, width=200, height=600, bd=0, highlightbackground="black", bg="#2c69a5", highlightcolor="black",
                   highlightthickness=1)
menu_frame.pack(side=LEFT)

game_frame = Frame(root, width=500, height=500, bg="grey")
game_frame.pack(expand=True)

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
turn = "AI"

one_button = Button(game_frame, textvariable=expression_field1, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update1(symbol, my_board, 1))
one_button.grid(row=0, column=0, padx=1, pady=1)
two_button = Button(game_frame, textvariable=expression_field2, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update2(symbol, my_board, 2))
two_button.grid(row=0, column=1, padx=1, pady=1)
three_button = Button(game_frame, textvariable=expression_field3, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update3(symbol, my_board, 3))
three_button.grid(row=0, column=2, padx=1, pady=1)
four_button = Button(game_frame, textvariable=expression_field4, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update4(symbol, my_board, 4))
four_button.grid(row=1, column=0, padx=1, pady=1)
five_button = Button(game_frame, textvariable=expression_field5, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update5(symbol, my_board, 5))
five_button.grid(row=1, column=1, padx=1, pady=1)
six_button = Button(game_frame, textvariable=expression_field6, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update6(symbol, my_board, 6))
six_button.grid(row=1, column=2, padx=1, pady=1)
seven_button = Button(game_frame, textvariable=expression_field7, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update7(symbol, my_board, 7))
seven_button.grid(row=2, column=0, padx=1, pady=1)
eight_button = Button(game_frame, textvariable=expression_field8, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update8(symbol, my_board, 8))
eight_button.grid(row=2, column=1, padx=1, pady=1)
nine_button = Button(game_frame, textvariable=expression_field9, fg="black", width=12, height=6, bd=0, bg="#eee", cursor="hand2", command=lambda: update9(symbol, my_board, 9))
nine_button.grid(row=2, column=2, padx=1, pady=1)

root.mainloop()
