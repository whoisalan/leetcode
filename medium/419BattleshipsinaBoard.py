# 有朝一日，我也能写出绝妙的算法

class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        num=0
        row=len(board)
        col=len(board[0])
        def func(x,y,num):
           while y<col-1 and board[x][y+1]=='X':
               y = y+1
               board[x][y]=num
           while x<row-1 and board[x+1][y]=='X':
               x=x+1
               board[x][y]=num
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    func(i,j,num)
                    num+=1
        
       
        
        return num