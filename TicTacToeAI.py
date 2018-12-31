#STEPHEN GUARDUCCI
#CS 370-101
#Project 1
#Tic Tac Toe AI
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from tkinter import messagebox
import os, signal
import collections

#Button-click event handler    
def click(CELL):
    
#User makes a move
    if CELL["text"] == " ":
        CELL["text"] = "X"
    else:
        return

#User win
    #Row win
    if CELL1["text"] == "X" and CELL2["text"] == "X" and CELL3["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL4["text"] == "X" and CELL5["text"] == "X" and CELL6["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL7["text"] == "X" and CELL8["text"] == "X" and CELL9["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    #Column win
    elif CELL1["text"] == "X" and CELL4["text"] == "X" and CELL7["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL2["text"] == "X" and CELL5["text"] == "X" and CELL8["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL3["text"] == "X" and CELL6["text"] == "X" and CELL9["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    #Diagonal win  
    elif CELL1["text"] == "X" and CELL5["text"] == "X" and CELL9["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL3["text"] == "X" and CELL5["text"] == "X" and CELL7["text"] == "X":
        messagebox.showinfo("Game Over", "You won the game!")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)


#Computer makes a move(AI)

    
    #Row Offense
    if buttons[0]["text"] == "O" and buttons[1]["text"] == "O" and buttons[2]["text"] == " ":
        buttons[2]["text"] = "O"
    elif buttons[1]["text"] == "O" and buttons[2]["text"] == "O" and buttons[0]["text"] == " ":
        buttons[0]["text"] = "O"
    elif buttons[0]["text"] == "O" and buttons[2]["text"] == "O" and buttons[1]["text"] == " ":
        buttons[1]["text"] = "O"
            
    elif buttons[3]["text"] == "O" and buttons[4]["text"] == "O" and buttons[5]["text"] == " ":
        buttons[5]["text"] = "O"
    elif buttons[4]["text"] == "O" and buttons[5]["text"] == "O" and buttons[3]["text"] == " ":
        buttons[3]["text"] = "O"
    elif buttons[3]["text"] == "O" and buttons[5]["text"] == "O" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"
            
    elif buttons[6]["text"] == "O" and buttons[7]["text"] == "O" and buttons[8]["text"] == " ":
        buttons[8]["text"] = "O"
    elif buttons[7]["text"] == "O" and buttons[8]["text"] == "O" and buttons[6]["text"] == " ":
        buttons[6]["text"] = "O"
    elif buttons[6]["text"] == "O" and buttons[8]["text"] == "O" and buttons[7]["text"] == " ":
        buttons[7]["text"] = "O"

    #Column Offense
    elif buttons[0]["text"] == "O" and buttons[3]["text"] == "O" and buttons[6]["text"] == " ":
        buttons[6]["text"] = "O"
    elif buttons[3]["text"] == "O" and buttons[6]["text"] == "O" and buttons[0]["text"] == " ":
        buttons[0]["text"] = "O"
    elif buttons[0]["text"] == "O" and buttons[6]["text"] == "O" and buttons[3]["text"] == " ":
        buttons[3]["text"] = "O"

    elif buttons[1]["text"] == "O" and buttons[4]["text"] == "O" and buttons[7]["text"] == " ":
        buttons[7]["text"] = "O"
    elif buttons[4]["text"] == "O" and buttons[7]["text"] == "O" and buttons[1]["text"] == " ":
        buttons[1]["text"] = "O"
    elif buttons[1]["text"] == "O" and buttons[7]["text"] == "O" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"

    elif buttons[2]["text"] == "O" and buttons[5]["text"] == "O" and buttons[8]["text"] == " ":
        buttons[8]["text"] = "O"
    elif buttons[5]["text"] == "O" and buttons[8]["text"] == "O" and buttons[2]["text"] == " ":
        buttons[2]["text"] = "O"
    elif buttons[2]["text"] == "O" and buttons[8]["text"] == "O" and buttons[5]["text"] == " ":
        buttons[5]["text"] = "O"

    #Diagonal Offense
    elif buttons[0]["text"] == "O" and buttons[4]["text"] == "O" and buttons[8]["text"] == " ":
        buttons[8]["text"] = "O"
    elif buttons[4]["text"] == "O" and buttons[8]["text"] == "O" and buttons[0]["text"] == " ":
        buttons[0]["text"] = "O"
    elif buttons[0]["text"] == "O" and buttons[8]["text"] == "O" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"

    elif buttons[2]["text"] == "O" and buttons[4]["text"] == "O" and buttons[6]["text"] == " ":
        buttons[6]["text"] = "O"
    elif buttons[4]["text"] == "O" and buttons[6]["text"] == "O" and buttons[2]["text"] == " ":
        buttons[2]["text"] = "O"
    elif buttons[2]["text"] == "O" and buttons[6]["text"] == "O" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"
        
            
    #Row Defense
    elif buttons[0]["text"] == "X" and buttons[1]["text"] == "X" and buttons[2]["text"] == " ":
        buttons[2]["text"] = "O"
    elif buttons[1]["text"] == "X" and buttons[2]["text"] == "X" and buttons[0]["text"] == " ":
        buttons[0]["text"] = "O"
    elif buttons[0]["text"] == "X" and buttons[2]["text"] == "X" and buttons[1]["text"] == " ":
        buttons[1]["text"] = "O"
            
    elif buttons[3]["text"] == "X" and buttons[4]["text"] == "X" and buttons[5]["text"] == " ":
        buttons[5]["text"] = "O"
    elif buttons[4]["text"] == "X" and buttons[5]["text"] == "X" and buttons[3]["text"] == " ":
        buttons[3]["text"] = "O"
    elif buttons[3]["text"] == "X" and buttons[5]["text"] == "X" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"
            
    elif buttons[6]["text"] == "X" and buttons[7]["text"] == "X" and buttons[8]["text"] == " ":
        buttons[8]["text"] = "O"
    elif buttons[7]["text"] == "X" and buttons[8]["text"] == "X" and buttons[6]["text"] == " ":
        buttons[6]["text"] = "O"
    elif buttons[6]["text"] == "X" and buttons[8]["text"] == "X" and buttons[7]["text"] == " ":
        buttons[7]["text"] = "O"

    #Column Defense
    elif buttons[0]["text"] == "X" and buttons[3]["text"] == "X" and buttons[6]["text"] == " ":
        buttons[6]["text"] = "O"
    elif buttons[3]["text"] == "X" and buttons[6]["text"] == "X" and buttons[0]["text"] == " ":
        buttons[0]["text"] = "O"
    elif buttons[0]["text"] == "X" and buttons[6]["text"] == "X" and buttons[3]["text"] == " ":
        buttons[3]["text"] = "O"

    elif buttons[1]["text"] == "X" and buttons[4]["text"] == "X" and buttons[7]["text"] == " ":
        buttons[7]["text"] = "O"
    elif buttons[4]["text"] == "X" and buttons[7]["text"] == "X" and buttons[1]["text"] == " ":
        buttons[1]["text"] = "O"
    elif buttons[1]["text"] == "X" and buttons[7]["text"] == "X" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"

    elif buttons[2]["text"] == "X" and buttons[5]["text"] == "X" and buttons[8]["text"] == " ":
        buttons[8]["text"] = "O"
    elif buttons[5]["text"] == "X" and buttons[8]["text"] == "X" and buttons[2]["text"] == " ":
        buttons[2]["text"] = "O"
    elif buttons[2]["text"] == "X" and buttons[8]["text"] == "X" and buttons[5]["text"] == " ":
        buttons[5]["text"] = "O"

    #Diagonal Defense
    elif buttons[0]["text"] == "X" and buttons[4]["text"] == "X" and buttons[8]["text"] == " ":
        buttons[8]["text"] = "O"
    elif buttons[4]["text"] == "X" and buttons[8]["text"] == "X" and buttons[0]["text"] == " ":
        buttons[0]["text"] = "O"
    elif buttons[0]["text"] == "X" and buttons[8]["text"] == "X" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"

    elif buttons[2]["text"] == "X" and buttons[4]["text"] == "X" and buttons[6]["text"] == " ":
        buttons[6]["text"] = "O"
    elif buttons[4]["text"] == "X" and buttons[6]["text"] == "X" and buttons[2]["text"] == " ":
        buttons[2]["text"] = "O"
    elif buttons[2]["text"] == "X" and buttons[6]["text"] == "X" and buttons[4]["text"] == " ":
        buttons[4]["text"] = "O"

    #Plays first open cell if no defensive or offensive move is available
    else:
        for entry in buttons:
            if entry["text"] == " ":
                entry["text"] = "O"
                break        
                
        
#Computer win
    #Row win
    if CELL1["text"] == "O" and CELL2["text"] == "O" and CELL3["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL4["text"] == "O" and CELL5["text"] == "O" and CELL6["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL7["text"] == "O" and CELL8["text"] == "O" and CELL9["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    #Column win
    elif CELL1["text"] == "O" and CELL4["text"] == "O" and CELL7["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL2["text"] == "O" and CELL5["text"] == "O" and CELL8["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL3["text"] == "O" and CELL6["text"] == "O" and CELL9["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    #Diagonal win  
    elif CELL1["text"] == "O" and CELL5["text"] == "O" and CELL9["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)
    elif CELL3["text"] == "O" and CELL5["text"] == "O" and CELL7["text"] == "O":
        messagebox.showinfo("Game Over", "You lost the game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)

#Tie
    if CELL1["text"] != " " and CELL2["text"] != " " and CELL3["text"] != " " and CELL4["text"] != " " and CELL5["text"] != " " and CELL6["text"] != " " and CELL7["text"] != " " and CELL8["text"] != " " and CELL9["text"] != " ":
        messagebox.showinfo("Game Over", "Tie game.")
        window.destroy()
        os.kill(os.getpid(), signal.SIGTERM)

        
        

      
#Window
window = Tk()
window.resizable(width = False, height = False)
window.title("Tic Tac Toe")
window.geometry("500x500")

#Grid
Grid.rowconfigure(window, 0, weight =1)
Grid.columnconfigure(window, 0, weight = 1)

#Frame
frame = Frame(window)
frame.grid(row = 0, column = 0, sticky = N+S+E+W)



#Row 0
Grid.rowconfigure(frame, 0, weight = 1)
Grid.columnconfigure(frame, 0, weight = 1)
CELL1 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL1), bg = "light blue")
CELL1.grid(row = 0, column = 0, sticky = N+S+E+W)

Grid.rowconfigure(frame, 0, weight = 1)
Grid.columnconfigure(frame, 1, weight = 1)
CELL2 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL2), bg = "light blue")
CELL2.grid(row = 0, column = 1, sticky = N+S+E+W)

Grid.rowconfigure(frame, 0, weight = 1)
Grid.columnconfigure(frame, 2, weight = 1)
CELL3 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL3), bg = "light blue")
CELL3.grid(row = 0, column = 2, sticky = N+S+E+W)



#Row 1
Grid.rowconfigure(frame, 1, weight = 1)
Grid.columnconfigure(frame, 0, weight = 1)
CELL4 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL4), bg = "light blue")
CELL4.grid(row = 1, column = 0, sticky = N+S+E+W)

Grid.rowconfigure(frame, 1, weight = 1)
Grid.columnconfigure(frame, 1, weight = 1)
CELL5 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL5), bg = "light blue")
CELL5.grid(row = 1, column = 1, sticky = N+S+E+W)

Grid.rowconfigure(frame, 1, weight = 1)
Grid.columnconfigure(frame, 2, weight = 1)
CELL6 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL6), bg = "light blue")
CELL6.grid(row = 1, column = 2, sticky = N+S+E+W)




#Row 2
Grid.rowconfigure(frame, 2, weight = 1)
Grid.columnconfigure(frame, 0, weight = 1)
CELL7 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL7), bg = "light blue")
CELL7.grid(row = 2, column = 0, sticky = N+S+E+W)

Grid.rowconfigure(frame, 2, weight = 1)
Grid.columnconfigure(frame, 1, weight = 1)
CELL8 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL8), bg = "light blue")
CELL8.grid(row = 2, column = 1, sticky = N+S+E+W)

Grid.rowconfigure(frame, 2, weight = 1)
Grid.columnconfigure(frame, 2, weight = 1)
CELL9 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL9), bg = "light blue")
CELL9.grid(row = 2, column = 2, sticky = N+S+E+W)


#Tuple of buttons
buttons = (CELL1, CELL2, CELL3, CELL4, CELL5, CELL6, CELL7, CELL8, CELL9)


window.mainloop()
