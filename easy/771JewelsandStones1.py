


# count,内置函数，遍历的意思

def numJewelsInStones(self, J, S):
    return sum(map(J.count, S))



def numJewelsInStones(self, J, S):
    return sum(map(S.count, J))             



def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)