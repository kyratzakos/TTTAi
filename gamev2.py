from tkinter import *
from tkinter import font
import customtkinter
from tic_tac_toe import *
import webbrowser


def nextstep(board):
    # This function will be called each time after the user's turn
    global buttons
    if game_is_over(board):
        # This part will disable the buttons, when the game is over
        for button in buttons:
            button.configure(state="disabled", bg="#bcbcbc")

    global turn
    start_button.configure(state="disabled", bg="#bcbcbc")
    if turn == "AI" and not game_is_over(board):
        turn = "Player"
        move = minimax(board, True)[1]
        select_space(board, move, "O")
        update("O", board, move, buttons[move-1], expression_fields[move-1])
    else:
        turn = "AI"

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

def label_clicked(event):
    # Making the credit label clickable
    webbrowser.open_new(r"https://www.github.com/kyratzakos")


if __name__ == '__main__':
    # Window settings
    customtkinter.set_appearance_mode("dark")
    root = customtkinter.CTk()
    root.geometry('800x600')
    root.resizable(False, False)
    root.title("Tic Tac Toe Game v2")
    root.iconbitmap(default="icon2.ico")
    # Frame settings
    menu_frame = Frame(root, width=200, height=600, bd=0, highlightbackground="black", bg="#2c69a5", highlightcolor="black",
                       highlightthickness=1)
    menu_frame.pack(side=LEFT)
    game_frame = Frame(root, width=500, height=500, bg="grey")
    game_frame.pack(expand=True)
    startgame_frame = Frame(root, width=200, height=100, bg="grey")
    startgame_frame.pack(expand=True)
    # Label settings
    label_font = font.Font(underline=True, size=9,)
    label = Label(menu_frame, text="Welcome to TicTacToe Game v2", bg="#2c69a5", bd=0, font="Calibri 14", wraplength=200)
    label.place(relx= 0.5, rely= 0.05, anchor="n")
    label2 = Label(menu_frame, text="Create in Python and tkinter", bg="#2c69a5", bd=0, font="Calibri 10")
    label2.place(relx=0.5, rely=0.15, anchor="n")
    label3 = Label(menu_frame, text="Created by Apostolos Kyratzakos \ngithub.com/kyratzakos", bg="#2c69a5", bd=0, font=label_font, cursor="hand2")
    label3.bind("<Button-1>", label_clicked)
    label3.place(relx=0.5, rely=0.94, anchor="center")
    # Game settings and variable creation
    expression_fields = [StringVar() for _ in range(9)]
    symbol = "X"
    turn = "AI"
    my_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    # Button settings
    buttons = []
    for i in range(9):
        button = create_button(i // 3, i % 3, i)
        buttons.append(button)

    start_button = Button(startgame_frame, text="Start Game!", fg="black", width=15, height=5, bd=0, bg="grey", cursor="hand2", command=lambda: nextstep(my_board))
    start_button.grid(padx=1, pady=1)
    root.mainloop()