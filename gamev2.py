import tkinter
from tkinter import *
import customtkinter

def update1(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field1.set(symbol)

def update2(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field2.set(symbol)

def update3(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field3.set(symbol)

def update4(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field4.set(symbol)

def update5(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field5.set(symbol)

def update6(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field6.set(symbol)

def update7(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field7.set(symbol)

def update8(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field8.set(symbol)

def update9(symbol):
    global expression
    expression = expression + str(symbol)
    expression_field9.set(symbol)


customtkinter.set_appearance_mode("dark")
root = customtkinter.CTk()
root.geometry('800x600')
root.resizable(0,0)
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

one_button = tkinter.Button(game_frame, textvariable = expression_field1, fg= "black", width= 12, height= 6, bd= 0, bg= "#eee", cursor = "hand2", command = lambda: update1(symbol)).grid(row = 0, column = 0, padx = 1, pady = 1)
two_button = Button(game_frame, textvariable = expression_field2, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update2(symbol)).grid(row = 0, column = 1, padx = 1, pady = 1)
three_button = Button(game_frame, textvariable = expression_field3, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update3(symbol)).grid(row = 0, column = 2, padx = 1, pady = 1)
four_button = Button(game_frame, textvariable = expression_field4, fg= "black", width= 12, height= 6, bd= 0, bg= "#eee", cursor = "hand2", command = lambda: update4(symbol)).grid(row = 1, column = 0, padx = 1, pady = 1)
five_button = Button(game_frame, textvariable = expression_field5, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update5(symbol)).grid(row = 1, column = 1, padx = 1, pady = 1)
six_button = Button(game_frame, textvariable = expression_field6, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update6(symbol)).grid(row = 1, column = 2, padx = 1, pady = 1)
seven_button = Button(game_frame, textvariable = expression_field7, fg= "black", width= 12, height= 6, bd= 0, bg= "#eee", cursor = "hand2", command = lambda: update7(symbol)).grid(row = 2, column = 0, padx = 1, pady = 1)
eight_button = Button(game_frame, textvariable = expression_field8, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update8(symbol)).grid(row = 2, column = 1, padx = 1, pady = 1)
nine_button = Button(game_frame, textvariable = expression_field9, fg= "black", width= 12, height = 6, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: update9(symbol)).grid(row = 2, column = 2, padx = 1, pady = 1)




#button1 = customtkinter.CTkButton(master=root, text='Hello world', font=('Inter', 14))
#button1.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()