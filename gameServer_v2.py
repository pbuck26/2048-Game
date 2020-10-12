#!/usr/bin/env python2
from gameCalculator import addNewSquare, recalculateSquares

import curses
import copy

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
curses.start_color()
#curses.use_default_colors()


screen.addstr("Lets get ready to rumble!!!!!\n\n\n")

#intitialize varibales
HighScore = 0
score     = 0
moves     = 0
board     = [[None,None,None, None],[None,None,None, None],[None,None,None, None], [None, None, None, None]]

def drawBoard(board, score):
    board = addNewSquare(board)
    displayboard = copy.deepcopy(board)
    for i in range(0,4):
        for j in range(0,4):
            if len(board[i]) <= 1:
                screen.addstr(board)
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
    screen.addstr('#################################\n\n\n')
    screen.addstr(' Press Q to quit')


def getUserName():
    curses.echo()
    screen.addstr(2,0, "Welcome to the thunderdome bitch\nEnter Username(10 char max):")
    screen.refresh
    username = screen.getstr(4, 0, 20)
    return username
    #screen.addstr(testString)
    #### color test #####
    #testString = str(6)
    #screen.addstr(testString, curses.color_pair(7))

# drawBoard(board)

######################################################################
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
######################################################################

username = getUserName()
#TODO: check if username exists
#TODO: grab leaderboard data from database.
#TODO: show leaderboard before game starts
#TODO: option selector?
#TODO: 

drawBoard(board, score)
board = addNewSquare(board)
while True:
    c = screen.getkey()
    if c == 'p':
        screen.addstr('stinky shit!\n')
        screen.erase()
        screen.refresh()
        drawBoard(board, score)
    elif c == 'q':
        break  # Exit the while loop
    elif c == 'KEY_LEFT' or c == 'KEY_RIGHT' or c == 'KEY_UP' or c == 'KEY_DOWN':
        boardCheck = copy.deepcopy(board)
        board,score = recalculateSquares(c, board, score)
        if board == boardCheck:
            if not any(None in sublist for sublist in board):
                screen.erase()
                screen.refresh()
                screen.addstr('GAME OVER IDIOT\n')
            else:
                continue # move didnt do anything
        screen.erase()
        screen.refresh()
        drawBoard(board, score)
    else:
        screen.addstr('INVALID KEY TRY AGAIN!!!!!\n')

# Terminate the curses module
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()