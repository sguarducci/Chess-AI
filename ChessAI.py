#STEPHEN GUARDUCCI
#CS 370-101
#Project 2
#Chess AI

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

from tkinter import messagebox
import time
import os, signal
import collections
import random

#PLAYER 1 (USER)
pawnTake = ()
pawnTake2 = ()
rookTakeRow = 100
rookTakeColumn = 100
knightTake = {}
bishopTake = {}
queenTake = {}
kingTake = {}
lastSelect = " "

#PLAYER 2 (COMPUTER)
rookTake = {}

def ComputerMove(buttons):

    d1 = True
    d2 = True
    d3 = True
    d4 = True

    r1 = True
    r2 = True
    
    for cell in buttons:
        curr_piece = cell['text']
        coordinates = buttons[cell]
        row = coordinates[0]
        column = coordinates[1]


        #KING MOVE

        
        #QUEEN MOVE

        
        #ROOK MOVE
        if cell["text"] == "♜":
            for cell2 in buttons:
                if r1 == True and buttons[cell2][0] == row and buttons[cell2][1] != column and cell2["text"] != " " and cell2["text"] != "♙" and cell2["text"] != "♖" and cell2["text"] != "♘" and cell2["text"] != "♗" and cell2["text"] != "♔" and cell2["text"] != "♕":
                    cell2["text"] = "♜"
                    cell["text"] = " "
                    break
                elif (buttons[cell2][0] == row and buttons[cell2][1] != column) and (cell2["text"] == "♟" or cell2["text"] == "♜" or cell2["text"] == "♞" or cell2["text"] == "♝" or cell2["text"]  == "♚" or cell2["text"] == "♛"):
                    r1 = False
                elif r2 == True and buttons[cell2][0] != row and buttons[cell2][1] == column and cell2["text"] != " " and cell2["text"] != "♙" and cell2["text"] != "♖" and cell2["text"] != "♘" and cell2["text"] != "♗" and cell2["text"] != "♔" and cell2["text"] != "♕":
                    cell2["text"] = "♜"
                    cell["text"] = " "
                    break
                elif (buttons[cell2][0] != row and buttons[cell2][1] == column) and (cell2["text"] == "♟" or cell2["text"] == "♜" or cell2["text"] == "♞" or cell2["text"] == "♝" or cell2["text"]  == "♚" or cell2["text"] == "♛"):
                    r2 = False
                elif (r1 == True and (buttons[cell2][0] == row and buttons[cell2][1] != column) or (r2 == True and buttons[cell2][0] != row and buttons[cell2][1] == column)) and cell2["text"] == " ":
                    cell2["text"] = "♜"
                    cell["text"] = " "
                    break


        #KNIGHT MOVE
        if cell["text"] == "♞":
            for cell2 in buttons:
                if((buttons[cell2][0] == row+2 and buttons[cell2][1] == column+1) or (buttons[cell2][0] == row+2 and buttons[cell2][1] == column-1) or (buttons[cell2][0] == row-2 and buttons[cell2][1] == column+1) or (buttons[cell2][0] == row-2 and buttons[cell2][1] == column-1) or (buttons[cell2][0] == row+1 and buttons[cell2][1] == column+2) or (buttons[cell2][0] == row+1 and buttons[cell2][1] == column-2) or (buttons[cell2][0] == row-1 and buttons[cell2][1] == column+2) or (buttons[cell2][0] == row-1 and buttons[cell2][1] == column-2)) and (cell2["text"] == "♙" or cell2["text"] == "♖" or cell2["text"] == "♘" or cell2["text"] == "♗" or cell2["text"]  == "♔" or cell2["text"] == "♕"):
                    cell2["text"] = "♞"
                    cell["text"] = " "
                    break
                elif((buttons[cell2][0] == row+2 and buttons[cell2][1] == column+1) or (buttons[cell2][0] == row+2 and buttons[cell2][1] == column-1) or (buttons[cell2][0] == row-2 and buttons[cell2][1] == column+1) or (buttons[cell2][0] == row-2 and buttons[cell2][1] == column-1) or (buttons[cell2][0] == row+1 and buttons[cell2][1] == column+2) or (buttons[cell2][0] == row+1 and buttons[cell2][1] == column-2) or (buttons[cell2][0] == row-1 and buttons[cell2][1] == column+2) or (buttons[cell2][0] == row-1 and buttons[cell2][1] == column-2)) and cell["text"] == " ":
                    cell["text"] = ""
                    break
                
        
        #BISHOP MOVE
            #BISHOP TAKES PIECE
            x = 1
            breakout = False
            while x <= 7 and breakout == False:
                for cell2 in buttons:
                    if d1 == True and (buttons[cell2][0] == row + x and buttons[cell2][1] == column + x) and (cell2["text"] == "♙" or cell2["text"] == "♖" or cell2["text"] == "♘" or cell2["text"] == "♗" or cell2["text"]  == "♔" or cell2["text"] == "♕"):
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        break
                    elif (buttons[cell2][0] == row + x and buttons[cell2][1] == column + x) and (cell2["text"] == "♟" or cell2["text"] == "♜" or cell2["text"] == "♞" or cell2["text"] == "♝" or cell2["text"]  == "♚" or cell2["text"] == "♛"):
                        d1 = False
                    elif d2 == True and (buttons[cell2][0] == row - x and buttons[cell2][1] == column - x) and (cell2["text"] == "♙" or cell2["text"] == "♖" or cell2["text"] == "♘" or cell2["text"] == "♗" or cell2["text"]  == "♔" or cell2["text"] == "♕"):
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        break
                    elif (buttons[cell2][0] == row - x and buttons[cell2][1] == column - x) and (cell2["text"] == "♟" or cell2["text"] == "♜" or cell2["text"] == "♞" or cell2["text"] == "♝" or cell2["text"]  == "♚" or cell2["text"] == "♛"):
                        d2 = False
                    elif d3 == True and (buttons[cell2][0] == row + x and buttons[cell2][1] == column - x) and (cell2["text"] == "♙" or cell2["text"] == "♖" or cell2["text"] == "♘" or cell2["text"] == "♗" or cell2["text"]  == "♔" or cell2["text"] == "♕"):
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        break
                    elif (buttons[cell2][0] == row + x and buttons[cell2][1] == column - x) and (cell2["text"] == "♟" or cell2["text"] == "♜" or cell2["text"] == "♞" or cell2["text"] == "♝" or cell2["text"]  == "♚" or cell2["text"] == "♛"):
                        d3 = False
                    elif d4 == True and (buttons[cell2][0] == row - x and buttons[cell2][1] == column + x) and (cell2["text"] == "♙" or cell2["text"] == "♖" or cell2["text"] == "♘" or cell2["text"] == "♗" or cell2["text"]  == "♔" or cell2["text"] == "♕"):
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        break
                    elif (buttons[cell2][0] == row - x and buttons[cell2][1] == column + x) and (cell2["text"] == "♟" or cell2["text"] == "♜" or cell2["text"] == "♞" or cell2["text"] == "♝" or cell2["text"]  == "♚" or cell2["text"] == "♛"):
                        d4 = False

                    
                    '''elif d1 == True and (buttons[cell2][0] == row + x and buttons[cell2][1] == column + x) and cell2["text"] == " ":
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        breakout = True
                        break
                    elif d2 == True and (buttons[cell2][0] == row - x and buttons[cell2][1] == column - x) and cell2["text"] == " ":
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        breakout = True
                        break
                    elif d3 == True and (buttons[cell2][0] == row + x and buttons[cell2][1] == column - x) and cell2["text"] == " ":
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        breakout = True
                        break
                    elif d4 == True and (buttons[cell2][0] == row - x and buttons[cell2][1] == column + x) and cell2["text"] == " ":
                        cell2["text"] = "♝"
                        cell["text"] = " "
                        breakout = True
                        break'''
                x = x + 1
        
        #PAWN MAKES MOVE
        if cell["text"] == "♟":
            rowInFront = row + 1
            rowTwoInFront = row + 2
            columnDiagonalRight = column - 1
            columnDiagonalLeft = column + 1
            #PAWN TAKES PIECE
            for cell2 in buttons:
                coordinates2 = buttons[cell2]
                if (coordinates2 == (rowInFront, columnDiagonalRight) or coordinates2 == (rowInFront, columnDiagonalLeft)) and (cell2["text"] == "♙" or cell2["text"] == "♖" or cell2["text"] == "♘" or cell2["text"] == "♗" or cell2["text"]  == "♔" or cell2["text"] == "♕"):
                    cell["text"] = " "
                    cell2["text"] = "♟"
                    break
            #PAWN MAKES MOVE
            for cell2 in buttons:
                coordinates2 = buttons[cell2]
                if cell2["text"] == " " and coordinates2 == (rowInFront, column):
                    cell["text"] = " "
                    cell2["text"] = "♟"
                    break
            break
         



d1 = True
d2 = True
d3 = True
d4 = True

r1 = True
r2 = True

def click(CURR_CELL, buttons):
    global lastSelect
    global pawnTake
    global pawnTake2
    global rookTakeRow
    global rookTakeColumn
    global knightTake
    global bishopTake
    global queenTake
    global kingTake
    pieces = {"Player 1" :{"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" },
              "Player 2" :{"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }}
    curr_piece = CURR_CELL['text']
    coordinates = buttons[CURR_CELL]
    row = coordinates[0]
    column = coordinates[1]
    
    #PLAYER SELECTS PAWN
    if curr_piece == pieces["Player 1"]["Pawn"] and lastSelect == " ":
        rowInFront = row - 1
        rowTwoInFront = row - 2
        columnDiagonalRight = column + 1
        columnDiagonalLeft = column - 1
        
        if row == 6:
            for cell in buttons:
                if buttons[cell] == (rowInFront,column) and cell["text"]  == " ":
                    cell["text"] = ""
                if buttons[cell] == (rowTwoInFront,column) and cell["text"] == " ":
                    cell["text"] = ""
                if buttons[cell] == (rowInFront,columnDiagonalRight) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    pawnTake = (rowInFront, columnDiagonalRight)
                if buttons[cell] == (rowInFront,columnDiagonalLeft) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    pawnTake2 = (rowInFront, columnDiagonalLeft)
            lastSelect = curr_piece
        
        else:
            for cell in buttons:
                if buttons[cell] == (rowInFront,column) and cell["text"]  == " ":
                    cell["text"] = ""
                if buttons[cell] == (rowInFront,columnDiagonalRight) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    pawnTake = (rowInFront, columnDiagonalRight)
                if buttons[cell] == (rowInFront,columnDiagonalLeft) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    pawnTake2 = (rowInFront, columnDiagonalLeft)
                lastSelect = curr_piece
                    
        CURR_CELL["text"] = " "

    #PLAYER SELECTS ROOK
    if curr_piece == pieces["Player 1"]["Rook"] and lastSelect == " ":
        for cell in buttons:
            if ((buttons[cell][0] == row and buttons[cell][1] != column) or (buttons[cell][0] != row and buttons[cell][1] == column)) and cell["text"] == " ":
                cell["text"] = ""
            if buttons[cell][0] == row and buttons[cell][1] != column and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                rookTakeRow = row
            if buttons[cell][0] != row and buttons[cell][1] == column and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                rookTakeColumn = column
            lastSelect  = curr_piece
        CURR_CELL["text"] = " "

    #PLAYER SELECTS KNIGHT
    if curr_piece == pieces["Player 1"]["Knight"] and lastSelect == " ":
        for cell in buttons:
            if((buttons[cell][0] == row+2 and buttons[cell][1] == column+1) or (buttons[cell][0] == row+2 and buttons[cell][1] == column-1) or (buttons[cell][0] == row-2 and buttons[cell][1] == column+1) or (buttons[cell][0] == row-2 and buttons[cell][1] == column-1) or (buttons[cell][0] == row+1 and buttons[cell][1] == column+2) or (buttons[cell][0] == row+1 and buttons[cell][1] == column-2) or (buttons[cell][0] == row-1 and buttons[cell][1] == column+2) or (buttons[cell][0] == row-1 and buttons[cell][1] == column-2)) and cell["text"] == " ":
                cell["text"] = ""
            if((buttons[cell][0] == row+2 and buttons[cell][1] == column+1) or (buttons[cell][0] == row+2 and buttons[cell][1] == column-1) or (buttons[cell][0] == row-2 and buttons[cell][1] == column+1) or (buttons[cell][0] == row-2 and buttons[cell][1] == column-1) or (buttons[cell][0] == row+1 and buttons[cell][1] == column+2) or (buttons[cell][0] == row+1 and buttons[cell][1] == column-2) or (buttons[cell][0] == row-1 and buttons[cell][1] == column+2) or (buttons[cell][0] == row-1 and buttons[cell][1] == column-2)) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                knightTake[cell] = (buttons[cell][0], buttons[cell][1])
            lastSelect = curr_piece
        CURR_CELL["text"] = " "

    #PLAYER SELECTS BISHOP
    if curr_piece == pieces["Player 1"]["Bishop"] and lastSelect == " ":
        x = 1
        while x <= 7:
            for cell in buttons:
                if(buttons[cell][0] == row + x and buttons[cell][1] == column + x) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row - x and buttons[cell][1] == column - x) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row + x and buttons[cell][1] == column - x) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row - x and buttons[cell][1] == column + x) and cell["text"] == " ":
                    cell["text"] = ""
                if((buttons[cell][0] == row + x and buttons[cell][1] == column + x) or (buttons[cell][0] == row - x and buttons[cell][1] == column - x) or (buttons[cell][0] == row + x and buttons[cell][1] == column - x) or (buttons[cell][0] == row - x and buttons[cell][1] == column + x)) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    bishopTake[cell] = (buttons[cell][0], buttons[cell][1])
            x = x + 1
        lastSelect = curr_piece
        CURR_CELL["text"] = " "

    #PLAYER SELECTS QUEEN
    if curr_piece == pieces["Player 1"]["Queen"] and lastSelect == " ":
        x = 1
        while x <= 7:
            for cell in buttons:
                if ((buttons[cell][0] == row and buttons[cell][1] != column) or (buttons[cell][0] != row and buttons[cell][1] == column)) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row + x and buttons[cell][1] == column + x) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row - x and buttons[cell][1] == column - x) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row + x and buttons[cell][1] == column - x) and cell["text"] == " ":
                    cell["text"] = ""
                if(buttons[cell][0] == row - x and buttons[cell][1] == column + x) and cell["text"] == " ":
                    cell["text"] = ""
                if buttons[cell][0] == row and buttons[cell][1] != column and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    queenTake[cell] = (row, buttons[cell][1])
                if buttons[cell][0] != row and buttons[cell][1] == column and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    queenTake[cell] = (buttons[cell][0], column)
                if((buttons[cell][0] == row + x and buttons[cell][1] == column + x) or (buttons[cell][0] == row - x and buttons[cell][1] == column - x) or (buttons[cell][0] == row + x and buttons[cell][1] == column - x) or (buttons[cell][0] == row - x and buttons[cell][1] == column + x)) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                    queenTake[cell] = (buttons[cell][0], buttons[cell][1])
            x = x + 1
        lastSelect = curr_piece
        CURR_CELL["text"] = " "
        
    #PLAYER SELECTS KING
    if curr_piece == pieces["Player 1"]["King"] and lastSelect == " ":
        for cell in buttons:
            if ((buttons[cell][0] == row - 1 and buttons[cell][1] == column - 1) or (buttons[cell][0] == row - 1 and buttons[cell][1] == column) or (buttons[cell][0] == row - 1 and buttons[cell][1] == column + 1) or (buttons[cell][0] == row and buttons[cell][1] == column - 1) or (buttons[cell][0] == row and buttons[cell][1] == column + 1) or (buttons[cell][0] == row + 1 and buttons[cell][1] == column - 1) or (buttons[cell][0] == row + 1 and buttons[cell][1] == column) or (buttons[cell][0] == row + 1 and buttons[cell][1] == column + 1)) and cell["text"] == " ":
                cell["text"] = ""
            if ((buttons[cell][0] == row - 1 and buttons[cell][1] == column - 1) or (buttons[cell][0] == row - 1 and buttons[cell][1] == column) or (buttons[cell][0] == row - 1 and buttons[cell][1] == column + 1) or (buttons[cell][0] == row and buttons[cell][1] == column - 1) or (buttons[cell][0] == row and buttons[cell][1] == column + 1) or (buttons[cell][0] == row + 1 and buttons[cell][1] == column - 1) or (buttons[cell][0] == row + 1 and buttons[cell][1] == column) or (buttons[cell][0] == row + 1 and buttons[cell][1] == column + 1)) and cell["text"] != " " and cell["text"] != "♙" and cell["text"] != "♖" and cell ["text"] != "♘" and cell["text"] != "♗" and cell["text"] != "♔" and cell["text"] != "♕":
                kingTake[cell] = (buttons[cell][0], buttons[cell][1])
        lastSelect = curr_piece
        CURR_CELL["text"] = " "


    #PLAYER MOVES PIECE
    if CURR_CELL["text"] == "":
        CURR_CELL["text"] = lastSelect
        for cell in buttons:
            if cell["text"] == "":
                cell["text"] = " "
        lastSelect = " "
        ComputerMove(buttons)

    #PAWN TAKES PIECE
    elif CURR_CELL["text"] != " " and CURR_CELL["text"] != "♙" and CURR_CELL["text"] != "♖" and CURR_CELL["text"] != "♘" and CURR_CELL["text"] != "♗" and CURR_CELL["text"] != "♔" and CURR_CELL["text"] != "♕" and (pawnTake == (row, column) or pawnTake2 == (row, column)):
        CURR_CELL["text"] = "♙"
        pawnTake = ()
        pawnTake2 = ()
        lastSelect = " "
        ComputerMove(buttons)

    #ROOK TAKES PIECE
    elif CURR_CELL["text"] != " " and CURR_CELL["text"] != "♙" and CURR_CELL["text"] != "♖" and CURR_CELL["text"] != "♘" and CURR_CELL["text"] != "♗" and CURR_CELL["text"] != "♔" and CURR_CELL["text"] != "♕" and (rookTakeRow == row or rookTakeColumn == column):
        CURR_CELL["text"] = "♖"
        rookTakeRow = 100
        rookTakeColumn = 100
        lastSelect = " "
        ComputerMove(buttons)

    #KNIGHT TAKES PIECE
    elif CURR_CELL["text"] != " " and CURR_CELL["text"] != "♙" and CURR_CELL["text"] != "♖" and CURR_CELL["text"] != "♘" and CURR_CELL["text"] != "♗" and CURR_CELL["text"] != "♔" and CURR_CELL["text"] != "♕" and lastSelect == "♘":
        for value in knightTake:
            if row == knightTake[value][0] and column == knightTake[value][1]:
                CURR_CELL["text"] = "♘"
                knightTake = {}
                break
        lastSelect = " "
        ComputerMove(buttons)
        
    #BISHOP TAKES PIECE
    elif CURR_CELL["text"] != " " and CURR_CELL["text"] != "♙" and CURR_CELL["text"] != "♖" and CURR_CELL["text"] != "♘" and CURR_CELL["text"] != "♗" and CURR_CELL["text"] != "♔" and CURR_CELL["text"] != "♕" and lastSelect == "♗":
        for value in bishopTake:
            if row == bishopTake[value][0] and column == bishopTake[value][1]:
                CURR_CELL["text"] = "♗"
                bishopTake = {}
                break
        lastSelect = " "
        ComputerMove(buttons)

    #QUEEN TAKES PIECE
    elif CURR_CELL["text"] != " " and CURR_CELL["text"] != "♙" and CURR_CELL["text"] != "♖" and CURR_CELL["text"] != "♘" and CURR_CELL["text"] != "♗" and CURR_CELL["text"] != "♔" and CURR_CELL["text"] != "♕" and lastSelect == "♕":
        for value in queenTake:
            if row == queenTake[value][0] and column == queenTake[value][1]:
                CURR_CELL["text"] = "♕"
                queenTake = {}
                break
        lastSelect = " "
        ComputerMove(buttons)

    #KING TAKES PIECE
    elif CURR_CELL["text"] != " " and CURR_CELL["text"] != "♙" and CURR_CELL["text"] != "♖" and CURR_CELL["text"] != "♘" and CURR_CELL["text"] != "♗" and CURR_CELL["text"] != "♔" and CURR_CELL["text"] != "♕" and lastSelect == "♔":
        for value in kingTake:
            if row == kingTake[value][0] and column == kingTake[value][1]:
                CURR_CELL["text"] = "♔"
                kingTake = {}
                break
        lastSelect = " "
        ComputerMove(buttons)
    

    #PAWN BECOMES QUEEN
    if CURR_CELL["text"] == "♙" and row == 0:
        CURR_CELL["text"] = "♕"


#Window
window = Tk()
window.resizable(width = False, height = False)
window.title("Chess")

#Frame
frame = Frame(window)
frame.grid(row = 0, column = 0, sticky = N+S+E+W)
      

#Row 0
CELL1 = Button(frame, text = "♜", font = ("Helvetica 30 bold"), command = lambda:click(CELL1,buttons), bg = "white")
CELL1.grid(row = 0, column = 0, sticky = N+S+E+W)


CELL2 = Button(frame, text = "♞", font = ("Helvetica 30 bold"), command = lambda:click(CELL2,buttons), bg = "brown")
CELL2.grid(row = 0, column = 1, sticky = N+S+E+W)


CELL3 = Button(frame, text= "♝", font = ("Helvetica 30 bold"), command = lambda:click(CELL3,buttons), bg = "white")
CELL3.grid(row = 0, column = 2, sticky = N+S+E+W)


CELL4 = Button(frame, text = "♛", font = ("Helvetica 30 bold"), command = lambda:click(CELL4,buttons), bg = "brown")
CELL4.grid(row = 0, column = 3, sticky = N+S+E+W)


CELL5 = Button(frame, text = "♚", font = ("Helvetica 30 bold"), command = lambda:click(CELL5,buttons), bg = "white")
CELL5.grid(row = 0, column = 4, sticky = N+S+E+W)


CELL6 = Button(frame, text= "♝", font = ("Helvetica 30 bold"), command = lambda:click(CELL6,buttons), bg = "brown")
CELL6.grid(row = 0, column = 5, sticky = N+S+E+W)


CELL7 = Button(frame, text = "♞", font = ("Helvetica 30 bold"), command = lambda:click(CELL7,buttons), bg = "white")
CELL7.grid(row = 0, column = 6, sticky = N+S+E+W)


CELL8 = Button(frame, text = "♜", font = ("Helvetica 30 bold"), command = lambda:click(CELL8,buttons), bg = "brown")
CELL8.grid(row = 0, column = 7, sticky = N+S+E+W)


#Row 1

CELL9 = Button(frame, text = "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL9,buttons), bg = "brown")
CELL9.grid(row = 1, column = 0, sticky = N+S+E+W)


CELL10 = Button(frame, text = "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL10,buttons), bg = "white")
CELL10.grid(row = 1, column = 1, sticky = N+S+E+W)


CELL11 = Button(frame, text= "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL11,buttons), bg = "brown")
CELL11.grid(row = 1, column = 2, sticky = N+S+E+W)


CELL12 = Button(frame, text = "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL12,buttons), bg = "white")
CELL12.grid(row = 1, column = 3, sticky = N+S+E+W)


CELL13 = Button(frame, text = "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL13,buttons), bg = "brown")
CELL13.grid(row = 1, column = 4, sticky = N+S+E+W)


CELL14 = Button(frame, text= "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL14,buttons), bg = "white")
CELL14.grid(row = 1, column = 5, sticky = N+S+E+W)

CELL15 = Button(frame, text = "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL15,buttons), bg = "brown")
CELL15.grid(row = 1, column = 6, sticky = N+S+E+W)


CELL16 = Button(frame, text = "♟", font = ("Helvetica 30 bold"), command = lambda:click(CELL16,buttons), bg = "white")
CELL16.grid(row = 1, column = 7, sticky = N+S+E+W)


#Row 2

CELL17 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL17,buttons), bg = "white")
CELL17.grid(row = 2, column = 0, sticky = N+S+E+W)


CELL18 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL18,buttons), bg = "brown")
CELL18.grid(row = 2, column = 1, sticky = N+S+E+W)


CELL19 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL19,buttons), bg = "white")
CELL19.grid(row = 2, column = 2, sticky = N+S+E+W)


CELL20 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL20,buttons), bg = "brown")
CELL20.grid(row = 2, column = 3, sticky = N+S+E+W)


CELL21 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL21,buttons), bg = "white")
CELL21.grid(row = 2, column = 4, sticky = N+S+E+W)


CELL22 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL22,buttons), bg = "brown")
CELL22.grid(row = 2, column = 5, sticky = N+S+E+W)


CELL23 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL23,buttons), bg = "white")
CELL23.grid(row = 2, column = 6, sticky = N+S+E+W)


CELL24 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL24,buttons), bg = "brown")
CELL24.grid(row = 2, column = 7, sticky = N+S+E+W)



#Row 3

CELL25 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL25,buttons), bg = "brown")
CELL25.grid(row = 3, column = 0, sticky = N+S+E+W)


CELL26 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL26,buttons), bg = "white")
CELL26.grid(row = 3, column = 1, sticky = N+S+E+W)


CELL27 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL27,buttons), bg = "brown")
CELL27.grid(row = 3, column = 2, sticky = N+S+E+W)


CELL28 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL28,buttons), bg = "white")
CELL28.grid(row = 3, column = 3, sticky = N+S+E+W)


CELL29 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL29,buttons), bg = "brown")
CELL29.grid(row = 3, column = 4, sticky = N+S+E+W)


CELL30 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL30,buttons), bg = "white")
CELL30.grid(row = 3, column = 5, sticky = N+S+E+W)


CELL31 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL31,buttons), bg = "brown")
CELL31.grid(row = 3, column = 6, sticky = N+S+E+W)


CELL32 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL32,buttons), bg = "white")
CELL32.grid(row = 3, column = 7, sticky = N+S+E+W)



#Row 4

CELL33 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL33,buttons), bg = "white")
CELL33.grid(row = 4, column = 0, sticky = N+S+E+W)


CELL34 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL34,buttons), bg = "brown")
CELL34.grid(row = 4, column = 1, sticky = N+S+E+W)


CELL35 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL35,buttons), bg = "white")
CELL35.grid(row = 4, column = 2, sticky = N+S+E+W)


CELL36 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL36,buttons), bg = "brown")
CELL36.grid(row = 4, column = 3, sticky = N+S+E+W)


CELL37 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL37,buttons), bg = "white")
CELL37.grid(row = 4, column = 4, sticky = N+S+E+W)


CELL38 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL38,buttons), bg = "brown")
CELL38.grid(row = 4, column = 5, sticky = N+S+E+W)


CELL39 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL39,buttons), bg = "white")
CELL39.grid(row = 4, column = 6, sticky = N+S+E+W)


CELL40 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL40,buttons), bg = "brown")
CELL40.grid(row = 4, column = 7, sticky = N+S+E+W)



#Row 5

CELL41 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL41,buttons), bg = "brown")
CELL41.grid(row = 5, column = 0, sticky = N+S+E+W)


CELL42 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL42,buttons), bg = "white")
CELL42.grid(row = 5, column = 1, sticky = N+S+E+W)


CELL43 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL43,buttons), bg = "brown")
CELL43.grid(row = 5, column = 2, sticky = N+S+E+W)


CELL44 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL44,buttons), bg = "white")
CELL44.grid(row = 5, column = 3, sticky = N+S+E+W)


CELL45 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL45,buttons), bg = "brown")
CELL45.grid(row = 5, column = 4, sticky = N+S+E+W)


CELL46 = Button(frame, text= " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL46,buttons), bg = "white")
CELL46.grid(row = 5, column = 5, sticky = N+S+E+W)


CELL47 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL47,buttons), bg = "brown")
CELL47.grid(row = 5, column = 6, sticky = N+S+E+W)


CELL48 = Button(frame, text = " ", font = ("Helvetica 30 bold"), command = lambda:click(CELL48,buttons), bg = "white")
CELL48.grid(row = 5, column = 7, sticky = N+S+E+W)



#Row 6

CELL49 = Button(frame, text = "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL49,buttons), bg = "white")
CELL49.grid(row = 6, column = 0, sticky = N+S+E+W)


CELL50 = Button(frame, text = "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL50,buttons), bg = "brown")
CELL50.grid(row = 6, column = 1, sticky = N+S+E+W)


CELL51 = Button(frame, text= "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL51,buttons), bg = "white")
CELL51.grid(row = 6, column = 2, sticky = N+S+E+W)


CELL52 = Button(frame, text = "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL52,buttons), bg = "brown")
CELL52.grid(row = 6, column = 3, sticky = N+S+E+W)


CELL53 = Button(frame, text = "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL53,buttons), bg = "white")
CELL53.grid(row = 6, column = 4, sticky = N+S+E+W)


CELL54 = Button(frame, text= "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL54,buttons), bg = "brown")
CELL54.grid(row = 6, column = 5, sticky = N+S+E+W)


CELL55 = Button(frame, text = "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL55,buttons), bg = "white")
CELL55.grid(row = 6, column = 6, sticky = N+S+E+W)


CELL56 = Button(frame, text = "♙", font = ("Helvetica 30 bold"), command = lambda:click(CELL56,buttons), bg = "brown")
CELL56.grid(row = 6, column = 7, sticky = N+S+E+W)



#Row 7

CELL57 = Button(frame, text = "♖", font = ("Helvetica 30 bold"), command = lambda:click(CELL57,buttons), bg = "brown")
CELL57.grid(row = 7, column = 0, sticky = N+S+E+W)


CELL58 = Button(frame, text = "♘", font = ("Helvetica 30 bold"), command = lambda:click(CELL58,buttons), bg = "white")
CELL58.grid(row = 7, column = 1, sticky = N+S+E+W)


CELL59 = Button(frame, text= "♗", font = ("Helvetica 30 bold"), command = lambda:click(CELL59,buttons), bg = "brown")
CELL59.grid(row = 7, column = 2, sticky = N+S+E+W)


CELL60 = Button(frame, text = "♕", font = ("Helvetica 30 bold"), command = lambda:click(CELL60,buttons), bg = "white")
CELL60.grid(row = 7, column = 3, sticky = N+S+E+W)


CELL61 = Button(frame, text = "♔", font = ("Helvetica 30 bold"), command = lambda:click(CELL61,buttons), bg = "brown")
CELL61.grid(row = 7, column = 4, sticky = N+S+E+W)


CELL62 = Button(frame, text= "♗", font = ("Helvetica 30 bold"), command = lambda:click(CELL62,buttons), bg = "white")
CELL62.grid(row = 7, column = 5, sticky = N+S+E+W)


CELL63 = Button(frame, text = "♘", font = ("Helvetica 30 bold"), command = lambda:click(CELL63,buttons), bg = "brown")
CELL63.grid(row = 7, column = 6, sticky = N+S+E+W)


CELL64 = Button(frame, text = "♖", font = ("Helvetica 30 bold"), command = lambda:click(CELL64,buttons), bg = "white")
CELL64.grid(row = 7, column = 7, sticky = N+S+E+W)





#Dictionary of buttons
buttons = {CELL1: (0,0), CELL2: (0,1), CELL3: (0,2), CELL4: (0,3), CELL5: (0,4), CELL6: (0,5), CELL7: (0,6), CELL8: (0,7), CELL9: (1,0), CELL10: (1,1), CELL11: (1,2), CELL12: (1,3), CELL13: (1,4), CELL14: (1,5), CELL15: (1,6), CELL16: (1,7), CELL17: (2,0), CELL18: (2,1), CELL19: (2,2), CELL20: (2,3), CELL21: (2,4), CELL22: (2,5), CELL23: (2,6), CELL24: (2,7), CELL25: (3,0), CELL26: (3,1), CELL27: (3,2), CELL28: (3,3), CELL29: (3,4), CELL30: (3,5), CELL31: (3,6), CELL32: (3,7), CELL33:  (4,0), CELL34: (4,1), CELL35: (4,2), CELL36: (4,3), CELL37: (4,4), CELL38: (4,5), CELL39: (4,6), CELL40: (4,7), CELL41: (5,0), CELL42: (5,1), CELL43: (5,2), CELL44: (5,3), CELL45: (5,4), CELL46: (5,5), CELL47: (5,6), CELL48: (5,7), CELL49: (6,0), CELL50: (6,1), CELL51: (6,2), CELL52: (6,3), CELL53: (6,4), CELL54: (6,5), CELL55: (6,6), CELL56: (6,7), CELL57: (7,0), CELL58: (7,1), CELL59: (7,2), CELL60: (7,3), CELL61: (7,4), CELL62: (7,5), CELL63: (7,6), CELL64: (7,7)}
messagebox.showinfo("Player 1", "Make the first move.")
#window.destroy()
#os.kill(os.getpid(), signal.SIGTERM)
window.mainloop()
