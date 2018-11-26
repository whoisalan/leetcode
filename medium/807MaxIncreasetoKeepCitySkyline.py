class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        front=[]
        side=[]

        row = len(grid)
        col = len(grid[0])

        diff=0

        for i in range(row):
            side.append(max(grid[i]))
        
        grid1 = list(zip(*grid))
        
        for i in range(col):
            front.append(max(grid1[i]))
        
        for i in range(row):
            for j in range(col):
                diff += min(front[i],side[j]) - grid[i][j]

        return diff


# 绝妙
def maxIncreaseKeepingSkyline(self, grid):
    row, col = map(max, grid), map(max, zip(*grid))
    return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))