
# dfs

def allPathsSourceTarget(self, graph):  
    res = []
    dfs(0, [0])

    def dfs(cur, path):
        if cur == len(graph) - 1: res.append(path)
        else:
            for i in graph[cur]: dfs(i, path + [i])
    
    return res

class Solution:
    def allPathsSourceTarget(self, graph, i = 0, q = [0]):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if i == 0: 
            global res
            res = []
        if i == len(graph) - 1: 
            res.append(q)
        for i in graph[i]: 
            self.allPathsSourceTarget(graph, i, q + [i])
        return res