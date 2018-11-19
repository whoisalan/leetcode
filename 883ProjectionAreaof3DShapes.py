# 看不懂
# class Solution:
#     def projectionArea(self, grid):
#         return sum(max(grid[i]) + max(row[i] for row in grid) + 
#         sum(v != 0 for v in grid[i]) for i in range(len(grid)))



a = [1,2,3]
b = [4,5,6]
zipped = zip(a,b) # 打包为元组的列表
# [(1, 4), (2, 5), (3, 6)]
zip(*zipped) # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
[(1, 2, 3), (4, 5, 6)]

def projectionArea(self, grid):
    return (sum(map(max, grid)) + sum(map(max, zip(*grid))) 
    + sum(v > 0 for row in grid for v in row))

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum = 0
        a = len(grid)
        b = len(grid[0])
        max = 0
        for i in range(a):
            for j in range(b):
                if grid[i][j] > 0:
                    sum += 1
                if grid[i][j] > max:
                    max = grid[i][j]      
            sum += max
            max = 0
        
        max = 0
        for j in range(b):
            for i in range(a):
                if grid[i][j] > max :
                    max = grid[i][j]
            sum += max
            max = 0
        

        return sum
