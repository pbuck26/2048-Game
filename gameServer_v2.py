#!/usr/bin/env python2
from gameCalculator import addNewSquare, recalculateSquares

import curses
import copy

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

def centerBoard():
    pass

def drawBoard(board):
    board = addNewSquare(board)
    displayboard = copy.deepcopy(board)
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == None:
                displayboard[i][j] = ' '
    screen.addstr('            2048\n')
    Display = 'Current score: {}  High Score: {}\n\n\n\n'.format(score, HighScore)
    screen.addstr(Display)


    toprow          = "#{}#{}#{}#{}#\n".format(str(displayboard[0][0]).center(7, ' '), str(displayboard[0][1]).center(7, ' '), str(displayboard[0][2]).center(7, ' '), str(displayboard[0][3]).center(7, ' '))
    middletoprow    = "#{}#{}#{}#{}#\n".format(str(displayboard[1][0]).center(7, ' '), str(displayboard[1][1]).center(7, ' '), str(displayboard[1][2]).center(7, ' '), str(displayboard[1][3]).center(7, ' '))
    middlebottomrow = "#{}#{}#{}#{}#\n".format(str(displayboard[2][0]).center(7, ' '), str(displayboard[2][1]).center(7, ' '), str(displayboard[2][2]).center(7, ' '), str(displayboard[2][3]).center(7, ' '))
    bottomrow       = "#{}#{}#{}#{}#\n".format(str(displayboard[3][0]).center(7, ' '), str(displayboard[3][1]).center(7, ' '), str(displayboard[3][2]).center(7, ' '), str(displayboard[3][3]).center(7, ' '))
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

# drawBoard(board)

# board = addNewSquare(board)

# for key in testInput:
#     print(str(board))
#     boardCheck = copy.deepcopy(board)
#     board = recalculateSquares(key, board)
#     print(str(board))
#     if board == boardCheck:
#         if not any(None in sublist for sublist in board):
#             print("game over")
#         else:
#             continue #move didnt do anything
#     else:
#         board = addNewSquare(board)

drawBoard(board)
board = addNewSquare(board)
while True:
    c = screen.getkey()
    if c == 'p':
        screen.addstr('stinky shit!\n')
        screen.erase()
        screen.refresh()
        drawBoard(board)
    elif c == 'q':
        break  # Exit the while loop
    elif c == 'KEY_LEFT' or c == 'KEY_RIGHT' or c == 'KEY_UP' or c == 'KEY_DOWN':
        boardCheck = copy.deepcopy(board)
        board = recalculateSquares(c, board)
        if board == boardCheck:
            if not any(None in sublist for sublist in board):
                screen.erase()
                screen.refresh()
                screen.addstr('GAME OVER IDIOT\n')
            else:
                continue # move didnt do anything
        screen.erase()
        screen.refresh()
        drawBoard(board)
    else:
        screen.addstr('INVALID KEY TRY AGAIN!!!!!\n')

# Terminate the curses module
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()