# import tkinter
from tkinter import *

# Create The Main Screen
root = Tk()
root.title('Main Window')
root.state('zoomed')

# Create Start Game Function
def startgame():
    global rowlist, columnlist, won_list, b, won_l, buttons, i, j, reg, runtime, win, clicked, count, buttonsamount

    runtime = 0
    buttonsamount = 0
    win = False
    clicked = True
    count = 0

    # Convert The Row List To Int
    rowlist[0] = int(rowlist[0])
    columnlist[0] = int(columnlist[0])

    # Create The Board
    buttons = []
    for i in range(rowlist[0]):
        buttons.append(i)
        buttonsamount += 1
        buttons[i] = []
        for j in range(columnlist[0]):
            buttons[i].append(j)
            buttons[i][j] = Button(reg, text=" ", font=("Helvetica",20), height=3, width=7, bg="SystemButtonFace", command=lambda m=i, n = j: b_click(m,n))
            buttons[i][j].grid(row=i,column=j)

    # Create And Destroy The Win Label
    winlabel = Label(reg, text=" ")
    winlabel.destroy()
    clicked = True
    count = 0

    

    # Create Menu
    my_menu = Menu(reg)
    reg.config(menu=my_menu)

    # Create options menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Back To Main Menu", command=reg.destroy)
    options_menu.add_command(label="Reset Game", command=startgame)

def startAIgame():
    global rowlist1, columnlist1, won_list, b, won_l, buttons, i, j, AIW, runtime, win, clicked, count, buttonsamount
    global AIW

    runtime = 0
    buttonsamount = 0
    win = False
    clicked = True
    count = 0

    # Convert The Row List To Int
    rowlist1[0] = int(rowlist1[0])
    columnlist1[0] = int(columnlist1[0])

    # Create The Board
    buttons = []
    for i in range(rowlist1[0]):
        buttons.append(i)
        buttonsamount += 1
        buttons[i] = []
        for j in range(columnlist1[0]):
            buttons[i].append(j)
            buttons[i][j] = Button(AIW, text=" ", font=("Helvetica",20), height=3, width=7, bg="SystemButtonFace", command=lambda m=i, n = j: b_click_AI(m,n))
            buttons[i][j].grid(row=i,column=j)

    # Create And Destroy The Win Label
    winlabel = Label(AIW, text=" ")
    winlabel.destroy()
    clicked = True
    count = 0

    
    print(buttons)
    # Create Menu
    my_menu = Menu(AIW)
    AIW.config(menu=my_menu)

    # Create options menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Back To Main Menu", command=AIW.destroy)
    options_menu.add_command(label="Reset Game", command=startgame)
# X starts so true
clicked = True
count = 0

# Check to see if someone won
def checkifwon(m,n):
    global runtime, win, winlabel, thewinnerprint, col, buttonsamount
    
    # Create a win and runtime object
    win = False
    runtime = 0
    locations = []

    # Check if any player won with a row
    for row in range(colsize-1):
        if board[m][row] == board[m][row+1]:
            locations.append(m)
            locations.append(n)
            runtime+=1
            if runtime == colsize-1:
                win = True
                for y in range(buttonsamount):
                    for dis in range(buttonsamount):
                        buttons[y][dis].config(state=DISABLED)
                winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                winlabel = Label(reg, text=winner, padx=10, font=("Helvetica",10), pady=10)
                winlabel.grid(row=m+10, column=0, columnspan=3, padx=10)
                runtime = 0 
                return 
            else:
                continue
        else:
            runtime = 0
            locations = []
            break

    # Check if any player won with a column
    for column in range(rowsize-1):
        if board[column][n] == board[column+1][n]:
            runtime+=1
            if runtime == rowsize-1:
                win = True
                for y in range(buttonsamount):
                   for dis in range(buttonsamount):
                       buttons[y][dis].config(state=DISABLED)
                winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                winlabel = Label(reg, text=winner, padx=10, font=("Helvetica",10), pady=10)
                winlabel.grid(row=i+1, column=0, columnspan=i+j, padx=10)
                runtime = 0 
                return
            else:
                continue
        else:
            runtime = 0
            break

    # Check if the board is 
    if rowsize == colsize:
        # Check if someone won with diagnol line from the left to right
        if m == n:
            for diag in range(rowsize-1):
                if board[diag][diag] == board[diag+1][diag+1]:
                    runtime += 1
                    if runtime == rowsize-1:
                        win = True
                        for y in range(buttonsamount):
                            for dis in range(buttonsamount):
                                buttons[y][dis].config(state=DISABLED)
                        winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                        winlabel = Label(reg, text=winner, padx=10, font=("Helvetica",10), pady=10)
                        winlabel.grid(row=i+1, column=0, columnspan=i+j, padx=10)
                        runtime = 0 
                        return
                    else:
                        continue
                else:
                    runtime = 0
                    break
                
        # Check if someone won with diagnol line from the right to left
        elif m == rowsize -1 - n:
            for diag in range(rowsize-1):
                if board[diag][rowsize-diag-1] == board[diag+1][rowsize-diag-2]:
                    runtime += 1
                    if runtime == rowsize-1:
                        win = True
                        for y in range(buttonsamount):
                            for dis in range(buttonsamount):
                                buttons[y][dis].config(state=DISABLED)
                        winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                        winlabel = Label(reg, text=winner, padx=10, font=("Helvetica",10), pady=10)
                        winlabel.grid(row=i+1, column=0, columnspan=i+j, padx=10)
                        runtime = 0 
                        return
                    else:
                        continue
                else:
                    runtime = 0
                    break

def checkifwonAI(m,n):
    global runtime, win, winlabel, thewinnerprint, col, buttonsamount, AIW
    
    # Create a win and runtime object
    win = False
    runtime = 0
    locations = []

    # Check if any player won with a row
    for row in range(colsize-1):
        if board[m][row] == board[m][row+1]:
            locations.append(m)
            locations.append(n)
            runtime+=1
            if runtime == colsize-1:
                win = True
                for y in range(buttonsamount):
                    for dis in range(buttonsamount):
                        buttons[y][dis].config(state=DISABLED)
                winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                winlabel = Label(AIW, text=winner, padx=10, font=("Helvetica",10), pady=10)
                winlabel.grid(row=m+10, column=0, columnspan=3, padx=10)
                runtime = 0 
                return 
            else:
                continue
        else:
            runtime = 0
            locations = []
            break

    # Check if any player won with a column
    for column in range(rowsize-1):
        if board[column][n] == board[column+1][n]:
            runtime+=1
            if runtime == rowsize-1:
                win = True
                for y in range(buttonsamount):
                   for dis in range(buttonsamount):
                       buttons[y][dis].config(state=DISABLED)
                winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                winlabel = Label(AIW, text=winner, padx=10, font=("Helvetica",10), pady=10)
                winlabel.grid(row=i+1, column=0, columnspan=i+j, padx=10)
                runtime = 0 
                return
            else:
                continue
        else:
            runtime = 0
            break

    # Check if the board is 
    if rowsize == colsize:
        # Check if someone won with diagnol line from the left to right
        if m == n:
            for diag in range(rowsize-1):
                if board[diag][diag] == board[diag+1][diag+1]:
                    runtime += 1
                    if runtime == rowsize-1:
                        win = True
                        for y in range(buttonsamount):
                            for dis in range(buttonsamount):
                                buttons[y][dis].config(state=DISABLED)
                        winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                        winlabel = Label(AIW, text=winner, padx=10, font=("Helvetica",10), pady=10)
                        winlabel.grid(row=i+1, column=0, columnspan=i+j, padx=10)
                        runtime = 0 
                        return
                    else:
                        continue
                else:
                    runtime = 0
                    break
                
        # Check if someone won with diagnol line from the right to left
        elif m == rowsize -1 - n:
            for diag in range(rowsize-1):
                if board[diag][rowsize-diag-1] == board[diag+1][rowsize-diag-2]:
                    runtime += 1
                    if runtime == rowsize-1:
                        win = True
                        for y in range(buttonsamount):
                            for dis in range(buttonsamount):
                                buttons[y][dis].config(state=DISABLED)
                        winner = ['The Winner Is... ' + buttons[m][n]["text"] + ' Player!! Congrats!']
                        winlabel = Label(AIW, text=winner, padx=10, font=("Helvetica",10), pady=10)
                        winlabel.grid(row=i+1, column=0, columnspan=i+j, padx=10)
                        runtime = 0 
                        return
                    else:
                        continue
                else:
                    runtime = 0
                    break

# Create b_click function
def b_click(m,n):
    global clicked, count, buttons, reg
    global won

    # Check If Its X or O
    if buttons[m][n]["text"] == " " and clicked == True:
        buttons[m][n]["text"] = "X"
        clicked = False
        count += 1
        buttons[m][n].config(state=DISABLED)
        board[m][n] = 1
        if count >= colsize*2-1 or count >= rowsize*2-1:
            checkifwon(m,n)
        
    elif buttons[m][n]["text"] == " " and clicked == False:
        buttons[m][n]["text"] = "O"
        clicked = True
        count += 1
        buttons[m][n].config(state=DISABLED)
        board[m][n] = 2
        if count >= colsize*2-1 or count >= rowsize*2-1:
            checkifwon(m,n)

# Create b_click function
def b_click_AI(m,n):
    global clicked, count, buttons, AIW
    global won

    # Check If Its X or O
    if buttons[m][n]["text"] == " " and clicked == True:
        buttons[m][n]["text"] = "X"
        clicked = False
        count += 1
        buttons[m][n].config(state=DISABLED)
        board[m][n] = 1
        if count >= colsize*2-1 or count >= rowsize*2-1:
            checkifwonAI(m,n)
        
    elif buttons[m][n]["text"] == " " and clicked == False:
        buttons[m][n]["text"] = "O"
        clicked = True
        count += 1
        buttons[m][n].config(state=DISABLED)
        board[m][n] = 2
        if count >= colsize*2-1 or count >= rowsize*2-1:
            checkifwonAI(m,n)

# Create List To Save The Size Of The Board 
columnlist = []
rowlist = []

def send():
    global columns, rows, columnlabel, rowlabel, send_b, restart, rowlist, columnlist, reg
    global board, colsize, rowsize, errors

    errors = 0
    error = Label()

    while int(rows.get()) >= 6 or int(columns.get()) >= 12:
            if int(rows.get()) >= 6:
                errors +=1
                if errors >= 2:
                    error = Label(reg, text="ERROR THE AMOUNT OF ROWS IS TO BIG")
                    error.grid(row=3, column=0, columnspan=2)
                    rows.delete(0, END)
                    rows.insert(0, "")
                    return
                else:
                    error = Label(reg, text="The Amount Of Rows Is To Big Please Try Again")
                    error.grid(row=3, column=0, columnspan=2)
                    rows.delete(0, END)
                    rows.insert(0, "")
                    return
            elif int(columns.get()) >= 12:
                errors +=1
                if errors >= 2:
                    error = Label(reg, text="ERROR THE AMOUNT OF COLUMNS IS TO BIG")
                    error.grid(row=3, column=0, columnspan=2)
                    columns.delete(0, END)
                    columns.insert(0, "")
                    return
                else:
                    error = Label(reg, text="The Amount Of Columns Is To Big Please Try Again")
                    error.grid(row=3, column=0, columnspan=2)
                    columns.delete(0, END)
                    columns.insert(0, "")
                    return

    # Save The Column Size And The Row Size
    columnlist.append(columns.get())

    rowlist.append(rows.get())

    columnlist[0] = int(columnlist[0])
    rowlist[0] = int(rowlist[0])

    rowsize, colsize = rowlist[0], columnlist[0]

    board = [[0 for j in range(colsize)] for i in range(rowsize)]

    # Print The Board
    # Destroy All Of The Screen
    columns.destroy()
    rows.destroy()
    columnlabel.destroy()
    error.grid_forget()
    rowlabel.destroy()
    send_b.grid_forget()
    

    
    # Run Start Game And Start The Game
    startgame()

def send_AI_Game():
    global columns1, rows1, columnlabel1, rowlabel1, send_b1, restart, rowlist1, columnlist1, AIW
    global board, colsize, rowsize, errors

    errors = 0
    error = Label()

    while int(rows1.get()) >= 6 or int(columns1.get()) >= 12:
            if int(rows1.get()) >= 6:
                errors +=1
                if errors >= 2:
                    error = Label(AIW, text="ERROR THE AMOUNT OF ROWS IS TO BIG")
                    error.grid(row=3, column=0, columnspan=2)
                    rows.delete(0, END)
                    rows.insert(0, "")
                    return
                else:
                    error = Label(AIW, text="The Amount Of Rows Is To Big Please Try Again")
                    error.grid(row=3, column=0, columnspan=2)
                    rows.delete(0, END)
                    rows.insert(0, "")
                    return
            elif int(columns1.get()) >= 12:
                errors +=1
                if errors >= 2:
                    error = Label(AIW, text="ERROR THE AMOUNT OF COLUMNS IS TO BIG")
                    error.grid(row=3, column=0, columnspan=2)
                    columns.delete(0, END)
                    columns.insert(0, "")
                    return
                else:
                    error = Label(AIW, text="The Amount Of Columns Is To Big Please Try Again")
                    error.grid(row=3, column=0, columnspan=2)
                    columns.delete(0, END)
                    columns.insert(0, "")
                    return

    # Save The Column Size And The Row Size
    columnlist1.append(columns1.get())

    rowlist1.append(rows1.get())

    columnlist1[0] = int(columnlist1[0])
    rowlist1[0] = int(rowlist1[0])

    rowsize, colsize = rowlist1[0], columnlist1[0]

    board = [[0 for j in range(colsize)] for i in range(rowsize)]

    # Print The Board
    # Destroy All Of The Screen
    columns1.destroy()
    rows1.destroy()
    columnlabel1.destroy()
    error.grid_forget()
    rowlabel1.destroy()
    send_b1.grid_forget()
    

    
    # Run Start Game And Start The Game
    startAIgame()

# Create a regular game function
def regular_game():
    global clicked, count, coulmns, rows, columnlabel, rowlabel, restart, rowlist, columnlist, reg
    clicked = True
    count = 0

    # Create another window
    reg = Toplevel()
    reg.title('Welcome To The Regular tic-tac-toe Game!!')

    #  Check The Size Of The Board That The Player Want To Play On
    def size():
        global clicked, count
        global winlabel, columns, rows, columnlabel, rowlabel, send_b, restart, rowlist, columnlist
        clicked = True
        count = 0

        columnlist = []
        columnlist.append(1)

        if columnlist[0] >= 1:
            columnlist.pop()

        rowlist = []
        rowlist.append(1)

        if rowlist[0] >= 1:
            rowlist.pop()

        # Create A Label
        rowlabel = Label(reg, text="Row Amount >>")
        rowlabel.grid(row=0, column=0)

        columnlabel = Label(reg, text="Column Amount >>")
        columnlabel.grid(row=1, column=0)

        # Create Entrys
        rows = Entry(reg, width = 10)
        rows.grid(row=0, column=1)

        columns = Entry(reg, width = 10)
        columns.grid(row=1, column=1)

        # Create A Send Button
        send_b = Button(reg, text="Confirm", command = send, width = 7)
        send_b.grid(row=2, column=0, columnspan=2)
        
       

    # Run Size
    size()

def AI_game():
    global clicked, count, coulmns1, rows1, columnlabel1, rowlabel1, restart, rowlist1, columnlist1, AIW
    clicked = True
    count = 0

    # Create another window
    AIW = Toplevel()
    AIW.title('Try To Beat Me! The AI!')

    #  Check The Size Of The Board That The Player Want To Play On
    def size():
        global clicked, count
        global winlabel, columns1, rows1, columnlabel1, rowlabel1, send_b1, restart, rowlist1, columnlist1,AIW
        clicked = True
        count = 0

        columnlist1 = []
        columnlist1.append(1)

        if columnlist1[0] >= 1:
            columnlist1.pop()

        rowlist1 = []
        rowlist1.append(1)

        if rowlist1[0] >= 1:
            rowlist1.pop()

        # Create A Label
        rowlabel1 = Label(AIW, text="Row Amount >>")
        rowlabel1.grid(row=0, column=0)

        columnlabel1 = Label(AIW, text="Column Amount >>")
        columnlabel1.grid(row=1, column=0)

        # Create Entrys
        rows1 = Entry(AIW, width = 10)
        rows1.grid(row=0, column=1)

        columns1 = Entry(AIW, width = 10)
        columns1.grid(row=1, column=1)

        # Create A Send Button
        send_b1 = Button(AIW, text="Confirm", command = send_AI_Game, width = 7)
        send_b1.grid(row=2, column=0, columnspan=2)
        
       

    # Run Size
    size()

clicked2 = True
count2 = 0

# Create a button for getting to the regular tic tac toe game
game_button = Button(root, text="Click For tic-tac-toe Game!", command=regular_game, padx=40, pady=20)
game_button.grid(row=0, column=0, columnspan=5, rowspan=3)

AI_game_button = Button(root, text="Click For Player VS AI Game!", command=AI_game, padx=40, pady=20)
AI_game_button.grid(row=6, column=0, columnspan=5, rowspan=3)

# Create a quit game button
qb = Button(root, text="Quit Game", command=root.destroy, padx=84, pady=20)
qb.grid(row=12, column=0, columnspan=5, rowspan=3)

mainloop()