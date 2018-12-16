

# 钥匙可能会出现重复的
class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [0]
        count = 0
        length = len(rooms)
        
        while keys:
            key = keys.pop(0)
            # for i in range(len(rooms[key])):
            #     keys.append(rooms[key][i])
            #     rooms[key][i]
            if len(rooms[key]) == 0:
                count += 1
                rooms[key].append("done")
            if rooms[key][0]!="done":
                it = iter(rooms[key])
                while True:
                    try:
                        i = next(it)
                        keys.append(i)
                    except StopIteration:
                        rooms[key][0]="done"
                        count += 1
                        break         


           

        return count == length


# ????!!!!!?????
# a = [0]
# it = iter(a)
# a.pop()
# print(next(it))