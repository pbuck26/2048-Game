#!/usr/bin/env python3
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

def drawBoard(board, score, HighScore):
    board = addNewSquare(board)
    displayboard = copy.deepcopy(board)
    for i in range(0,4):
        for j in range(0,4):
            if len(board[i]) <= 1:
                screen.addstr(board)
            if board[i][j] == None:
                displayboard[i][j] = ' '
    screen.addstr('\n\n\n            2048\n')
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
    screen.erase()
    return username

def getLeaderboard():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="patrickbuckley",
        password="",
        database="game2048"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM leaderboard ORDER BY score DESC")
    leaderboard = mycursor.fetchall()
    # show top 5
    #answer = screen.getstr("Show Leaderboard? (y/n", 1)
    #if answer == "n":
        #return
    screen.addstr('\n\n\n\nLEADERBOARD\n')
    screen.refresh
    count = 0
    HighScore = leaderboard[0][2]
    for x in leaderboard:
        count += 1
        scoreFormatted = str(count) + ": " + x[1] + " " + str(x[2]) + "\n"
        screen.addstr(scoreFormatted)
    
    screen.refresh
    return [HighScore, leaderboard]

def saveToDatabase(username, score):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost",
        user="patrickbuckley",
        password="",
        database="game2048"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO leaderboard (username, score) VALUES (%s, %s)"
    values = (username, str(score))
    mycursor.execute(sql, values)
    mydb.commit()
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

output = getLeaderboard()
HighScore = output[0]
leaderboard = output[1]

drawBoard(board, score, HighScore)
board = addNewSquare(board)
while True:
    c = screen.getkey()
    if c == 'p':
        screen.addstr('stinky shit!\n')
        screen.erase()
        screen.refresh()
        drawBoard(board, score, HighScore)
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
                break
            else:
                continue # move didnt do anything
        screen.erase()
        screen.refresh()
        drawBoard(board, score, HighScore)
    else:
        screen.addstr('INVALID KEY TRY AGAIN!!!!!\n')

screen.addstr("Would you like to save {}? (y/n)".format(username))
screen.refresh
answer = screen.getstr(0,4,20)

if answer == "y":
    saveToDatabase(username, score)



# Terminate the curses module
curses.nocbreak()
screen.keypad(False)
curses.echo()
curses.endwin()