class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        up = 0
        lr = 0 
        for i in moves:
            if i == "U":
                up = up +1
            elif i == "D":
                up = up -1
            elif i == "L":
                lr = lr + 1
            else:
                lr = lr -1
        
        return up==0 and lr==0
        
def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')