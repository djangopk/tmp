import os
import time

def printBoard(board, n):
    string = "-----"*n
    for i in range(0, n):
        if(i==0):
            print(string)
        for j in range(0, n):
            if(j==0):
                print("|", end=" ")
            print(board[i][j], end=" | ")
        print()
        # print("---------------------------------")
        print(string)
