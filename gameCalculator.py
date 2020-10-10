#!/usr/bin/env python3

import random
import copy

#########################
#calculator implementation
#########################

def addNewSquare(board):
    import random
    orderedEmptySquares = []
    # check num of empty squares
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == None:
                orderedEmptySquares.append([i, j])
    if not orderedEmptySquares:
        return
    
    # determine where to put random num
    randNums = [2, 4]
    newNum = randNums[random.randint(0,1)]
    resultSquare = random.randint(0, len(orderedEmptySquares)-1)
    board[orderedEmptySquares[resultSquare][0]][orderedEmptySquares[resultSquare][1]] = newNum
    return board

def shiftSquare(indexNeeded, flipIndexFlag, board):
    for i in range(0, 4):
        if flipIndexFlag:
            boardArray = board[i]
        else:
            boardArray = [row[i] for row in board]
        boardArray = [x for x in boardArray if x != None]
        #check if any merges can be made
        boardArray = mergeCheck(indexNeeded, boardArray)
        # add Nones back to list
        boardArray = addNones(boardArray, indexNeeded)
        # modify global board values
        for j in range(0,4):
            if flipIndexFlag:
                board[i][j] = boardArray[j]
            else:
                board[j][i] = boardArray[j]
    return board

def addNones(boardArray, indexNeeded):
    while len(boardArray) < 4:
        if indexNeeded == -1:
            indexNeeded = len(boardArray)
        boardArray.insert(indexNeeded, None)
    return boardArray


# input is 4x1 or less array
# output is array with all merges completed
def mergeCheck(indexNeeded, boardArray):
    print(str(boardArray))
    if indexNeeded == -1:
            boardArray.reverse()
    i = 1
    while i  < len(boardArray):
        if boardArray[i] == boardArray[i- 1]:
            boardArray[i-1] *= 2
            #remove duplicate
            del boardArray[i]
        i += 1
    if indexNeeded == -1:
        boardArray.reverse()
        print(str(boardArray))
    return boardArray

def recalculateSquares(keystroke, board):
    if keystroke == 'KEY_DOWN':
        listInsertIndex = 0
        flipIndexFlag = False
        board = shiftSquare(listInsertIndex, flipIndexFlag, board)

    elif keystroke == 'KEY_UP':
        listInsertIndex = -1
        flipIndexFlag = False
        shiftSquare(listInsertIndex, flipIndexFlag, board)

    elif keystroke == 'KEY_LEFT':
        listInsertIndex = -1
        flipIndexFlag = True
        shiftSquare(listInsertIndex, flipIndexFlag, board)

    elif keystroke == 'KEY_RIGHT':
        listInsertIndex = 0
        flipIndexFlag = True
        shiftSquare(listInsertIndex, flipIndexFlag, board)
    else:
        print("invalid key")
    return board

#intitialize varibales
HighScore = 0
score     = 0
moves     = 0
board     = [[None,None,None, None],[None,None,None, None],[None,None,None, None], [None, None, None, None]]
testInput = ['KEY_RIGHT', 'KEY_LEFT', 'KEY_UP', 'KEY_DOWN','KEY_RIGHT', 'KEY_LEFT', 'KEY_UP', 'KEY_DOWN']

board = addNewSquare(board)

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