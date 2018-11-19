# 底下这样写会出错的，可能foriin也是基于length的吧
# list = [1,2,3,4,5,6]
# for i in list:
#     print(i)
#     list.pop(0)



class RecentCounter:

    def __init__(self):
        self.p = collections.deque()  
              

    def ping(self, t):
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)


