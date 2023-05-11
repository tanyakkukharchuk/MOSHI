import random
from math import exp
from copy import deepcopy

n = 8
temp = 1

def ChessBoard(n):
    vector = list(range(n))
    random.shuffle(vector)
    print(vector)
    board = {}
    for _ in range(n): board[_] = vector[_]
    chessboardOutput(board)
    return board

def amoutOfThreats(n):
    return (n - 1) * n / 2

def toBePlaced(board):
    board_1 = {}
    board_2 = {}
    for i in board:
        counter_1 = i - board[i]
        if counter_1 not in board_1:
            board_1[counter_1] = 1
        else:
            board_1[counter_1] += 1
    for j in board:
        counter_2 = j + board[j]
        if counter_2 not in board_2:
            board_2[counter_2] = 1
        else:
            board_2[counter_2] += 1
    amount = 0
    for k in board_1:
        amount += amoutOfThreats(board_1[k])
    for k in board_2:
        amount += amoutOfThreats(board_2[k])
    return amount

def method():
    chessBoard = ChessBoard(n)
    chessThreats = toBePlaced(chessBoard)
    print(toBePlaced(chessBoard))
    t = temp
    tempIncrease = 0.99
    while t > 0:
        t *= tempIncrease
        bestSolution = deepcopy(chessBoard)
        i=0
        j=0
        while (i == j):
            i = random.randrange(0, n - 1)
            j = random.randrange(0, n - 1)
        bestSolution[i], bestSolution[j] = bestSolution[j], bestSolution[i]
        if toBePlaced(bestSolution) - chessThreats < 0 or random.uniform(0, 1) < exp(-(toBePlaced(bestSolution) - chessThreats) / t):
            chessBoard = deepcopy(bestSolution)
            chessThreats = toBePlaced(chessBoard)
        if chessThreats == 0:
            chessboardOutput(chessBoard)
            break

def chessboardOutput(board):
    print("{0}x{0} chess board output:".format(n))
    for k in board.values():
        print("□  " * k + "♕ " + "□  " * (n - k - 1))

method()
