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
   
  def solve(board, row, n):
    if(row>=n):
        return True

    for col in range(0, n):
        # printBoard(board, n)
        # time.sleep(0.01)
        # os.system("clear")
        if(isSafe(board, row, col , n)):
            board[row][col] = 1
            if(solve(board, row+1, n)):
                return True
            board[row][col] = 0
