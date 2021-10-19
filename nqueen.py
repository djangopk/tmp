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

def isSafe(board, row, col, n):
    for r in range(0, row):
        if(board[r][col] == 1):
            return False
    
    r=row
    c=col
    while(r>=0 and c>=0):
        if(board[r][c] == 1):
            return False
        r-=1
        c-=1

    r=row
    c=col
    while(r>=0 and c<n):
        if board[r][c] == 1:
            return False
        r-=1
        c+=1

    return True
    
def main():
    n = int(input("Enter The Number of Rows "))
    board = [[0 for i in range(0, n)]for j in range(0, n)]
    
    # printBoard(board, n)


    if(solve(board, 0, n)):
        printBoard(board, n)
    
    else:
        print("Can Not Be Solved")
        printBoard(board, n)


main()
