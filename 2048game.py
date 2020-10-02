#!/usr/bin/env python3

import curses
import random
import copy
import numpy as np

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

screen.addstr("Lets get ready to rumble!!!!!\n\n\n")

#intitialize varibales
HighScore = 0
score     = 0
moves     = 0
board     = [[None,None,None, None],[None,None,None, None],[None,None,None, None], [None, None, None, None]]

def addNewSquare():
    orderedEmptySquares = []
    # check num of empty squares
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == None:
                orderedEmptySquares.append([i, j])
    if len(orderedEmptySquares) == 0:
        return
    
    # determine where to put random num
    randNums = [2, 4]
    newNum = randNums[random.randint(0,1)]
    resultSquare = random.randint(0, len(orderedEmptySquares)-1)
    board[orderedEmptySquares[resultSquare][0]][orderedEmptySquares[resultSquare][1]] = newNum
    return board

#def shiftSquare(keystroke):
    # convert board to numpy matrix
    # once board is shifted then call recalculateSquares
    #numpyBoard = np.array(board, dtype=float)
    #logicalArray = np.isnan(numpyBoard)
    # find out what colums to look at
    #if keystroke == 'KEY_DOWN':
    #   all(logicalArray[:,]


def recalculateSquares(keystroke):
    if keystroke == 'KEY_DOWN':
        for i in range(0, 4):
            for j in range(0,4):
                if j == 3:
                    continue

                # first check if we can move down
                if board[j][i] != None and board[j+1][i] == None:
                    board[j+1][i] = board[j][i]
                    board[j][i] = None
                    continue
                
                # Then check if we can merge
                if board[j][i] == board[j+1][i] and board[j][i] != None:
                    board[j+1][i] = board[j][i]*2
                    board[j][i] = None
                    break # cause we only allow one merge for each row or column per turn

    elif keystroke == 'KEY_UP':
        for i in range(0, 4):
            for j in range(3, -1, -1):
                if j == 0:
                    continue

                # first check if we can move u
                if board[j][i] != None and board[j-1][i] == None:
                    board[j-1][i] = board[j][i]
                    board[j][i] = None
                    continue

                if board[j][i] == board[j-1][i] and board[j][i] != None:
                    board[j-1][i] = board[j][i]*2
                    board[j][i] = None
                    break

    elif keystroke == 'KEY_LEFT':
        for i in range(0, 4):
            for j in range(3, -1, -1):
                if j == 0:
                    continue

                if board[i][j] != None and board[i][j-1] == None:
                    board[i][j-1] = board[i][j]
                    board[i][j] = None
                    continue

                if board[i][j] == board[i][j-1] and board[i][j] != None:
                    board[i][j-1] = board[i][j]*2
                    board[i][j] = None
                    break
    elif keystroke == 'KEY_RIGHT':
        for i in range(0, 4):
            for j in range(0, 4):
                if j == 3:
                    continue
                if board[i][j] != None and board[i][j+1] == None:
                    board[i][j+1] = board[i][j]
                    board[i][j] = None
                    continue

                if board[i][j] == board[i][j+1] and board[i][j] != None:
                    board[i][j+1] = board[i][j]*2
                    board[i][j] = None
                    continue
    else:
        screen.addstr('INVALID KEY SELECT AGAIN')
        return
    

def drawBoard():
    addNewSquare()
    displayboard = copy.deepcopy(board)
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == None:
                displayboard[i][j] = ' '
    screen.addstr('            2048\n')
    Display = 'Current score: {}  High Score: {}\n\n\n\n'.format(score, HighScore)
    screen.addstr(Display)
    toprow    = "#   {}   #   {}   #   {}   #   {}   #\n".format(displayboard[0][0], displayboard[0][1], displayboard[0][2], displayboard[0][3])
    middletoprow = "#   {}   #   {}   #   {}   #   {}   #\n".format(displayboard[1][0], displayboard[1][1], displayboard[1][2], displayboard[1][3])
    middlebottomrow = "#   {}   #   {}   #   {}   #   {}   #\n".format(displayboard[2][0], displayboard[2][1], displayboard[2][2], displayboard[2][3])
    bottomrow = "#   {}   #   {}   #   {}   #   {}   #\n".format(displayboard[3][0], displayboard[3][1], displayboard[3][2], displayboard[3][3])
    screen.addstr('#################################\n')
    screen.addstr('#       #       #       #       #\n')
    screen.addstr(toprow)
    screen.addstr('#       #       #       #       #\n')
    screen.addstr('#################################\n')
    screen.addstr('#       #       #       #       #\n')
    screen.addstr(middletoprow)
    screen.addstr('#       #       #       #       #\n')
    screen.addstr('#################################\n')
    screen.addstr('#       #       #       #       #\n')
    screen.addstr(middlebottomrow)
    screen.addstr('#       #       #       #       #\n')
    screen.addstr('#################################\n')
    screen.addstr('#       #       #       #       #\n')
    screen.addstr(bottomrow)
    screen.addstr('#       #       #       #       #\n')
    screen.addstr('#################################\n')

drawBoard()
while True:
    c = screen.getkey()
    if c == 'p':
        screen.addstr('stinky!\n')
        screen.erase()
        screen.refresh()
        drawBoard()
    elif c == 'q':
        break  # Exit the while loop
    elif c == 'KEY_LEFT' or c == 'KEY_RIGHT' or c == 'KEY_UP' or c == 'KEY_DOWN':
        screen.erase()
        screen.refresh()
        recalculateSquares(c)
        drawBoard()
    else:
        screen.addstr('INVALID KEY TRY AGAIN!!!!!\n')

# Terminate the curses module
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()
