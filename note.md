## I probably won't read the code that i wrote, so this is for review
## this includes the some tricks or knowledge that i dont konw  
## Both english and chinese will be used,:(,sorry about that
--------------------------------------------


## enumertate:  
i,j 分别代表着下标和内容，发现比for好用一点
```
>>> for i,j in enumerate(('a','b','c')):
>>> print i,j
0 a
1 b
2 c
```
---------------------  
## 函数内部的函数，外部无法访问  
--------------------
## DFS：递归函数模型  
```
void dfs(int step)
{
    判断边界，如果到了边界当然直接返回啦
    尝试每一种可能结果for(i=0;i<n;i++)
    {
        处理当前步
        继续下一步dfs(step + 1)
    }
    返回
}
```
example:找到首结点到末结点的所有路径    
```
class Solution:
    def allPathsSourceTarget(self, graph, i = 0, q = [0]):
    #函数括号中可以标记默认的传参，如果外部没有传参，依照默认值来。函数内部也可以定义全局变量global
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
```
--------------------
## 列表<->字符串：  
```
"".join() #没有空格  
" ".join()#有空格
str.split(" ")
```
-------------------
## 二进制相关:  
第i位的值>前i-1位所有值之和  
int('',base)二进制转