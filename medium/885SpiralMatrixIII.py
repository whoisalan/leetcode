
# 正方向 和 负方向 可以合并计算
class Solution:
    def spiralMatrixIII(self, R=5, C=6, r0=0, c0=0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = []
        x = r0
        y = c0
        res.append([x,y])
        delta = 1
        flag = 1
        while len(res) < R*C:
        
            if flag ==1:
                for i in range(delta):
                    y += 1
                    if x<R and y<C and x>-1 and y>-1:
                        res.append([x,y])
                flag = 2        
            if flag ==2:
                for i in range(delta):
                    x += 1
                    if x<R and y<C and x>-1 and y>-1:
                        res.append([x,y])
                flag = 3
                delta+=1
            if flag ==3:
                for i in range(delta):
                    y -= 1
                    if x<R and y<C and x>-1 and y>-1:
                        res.append([x,y])
                flag = 4
                
            if flag ==4:
                for i in range(delta):
                    x -= 1
                    if x<R and y<C and x>-1 and y>-1:
                        res.append([x,y])
                flag = 1       
                delta += 1                 
                
        return res
