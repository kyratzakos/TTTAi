import tkinter
from tkinter import *
import customtkinter
from tic_tac_toe import *


def nextstep(board):
    # This function will be called each time after the user's turn
    global buttons
    if game_is_over(board):
        # This part will disable the buttons, when the game is over
        for button in buttons:
            button.configure(state="disabled", bg="#bcbcbc")

    global turn
    if turn == "AI" and not game_is_over(board):
        turn = "Player"
        move = minimax(board, True)[1]
        select_space(board, move, "O")
        update("O", board, move, buttons[move-1], expression_fields[move-1])
    else:
        turn = "AI"
    print_board(board)

def update(symbol, board, move, button, field):
    # This function will update the text variable of each button, whether the user or the AI presses it
    field.set(symbol)
    select_space(board, move, symbol)
    button.configure(state="disabled")
    nextstep(board)

def create_button(row, column, expression_field_index):
    # This function will create 9 buttons inside a 3x3 grid
    button = Button(
        game_frame,
        textvariable=expression_fields[expression_field_index],
        fg="black",
        width=12,
        height=6,
        bd=0,
        bg="#eee",
        cursor="hand2",
        command=lambda idx=expression_field_index: update(symbol, my_board, idx + 1, buttons[idx], expression_fields[idx])
    )
    button.grid(row=row, column=column, padx=1, pady=1)
    return button

if __name__ == '__main__':
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

    expression_fields = [StringVar() for _ in range(9)]
    symbol = "X"
    turn = "AI"
    my_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    buttons = []
    for i in range(9):
        button = create_button(i // 3, i % 3, i)
        buttons.append(button)

    root.mainloop()