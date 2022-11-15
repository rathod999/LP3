board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def isvalid(board,row,col):
    x = 0 
    y = 0
    while(x < len(board)):
        if board[x][col] == 1:
                return False
        x+=1
    while(y<len(board)):
        if board[row][y] == 1:
                return False
        y+=1
    x = row
    y = col
    while x >= 0 and x < len(board) and y>= 0 and y < len(board):
        if board[x][y] == 1:
            return False
        x+= 1
        y += 1
    x = row
    y = col
    while x >= 0 and x < len(board) and y>= 0 and y < len(board):
        if board[x][y] == 1:
            return False
        x-= 1
        y -= 1
    x = row
    y = col
    while x >= 0 and x < len(board) and y>= 0 and y < len(board):
        if board[x][y] == 1:
            return False
        x += 1
        y -= 1
    x = row
    y = col
    while x >= 0 and x < len(board) and y>= 0 and y < len(board):
        if board[x][y] == 1:
            return False
        x -= 1
        y += 1
    return True
def nqueen(board,row):
    if row == len(board):
        return True

    ind = 0
    while(ind < len(board)):
        if(isvalid(board,row,ind)):
            board[row][ind] = 1
            if nqueen(board,row+1):
                return True
            else:
                board[row][ind] = 0
        ind += 1
    return False        

nqueen(board,0)
for i in board:
    print(i)

