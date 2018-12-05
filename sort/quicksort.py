# def QuickSort(myList,start,end):
#     if start < end:
#         i,j = start,end
#         base = myList[i]
#         while i < j:
#             while (i < j) and (myList[j] >= base):
#                 j = j - 1
#             while (i < j) and (myList[i] <= base):
#                 i = i + 1
#             myList[j],myList[i] = myList[i],myList[j]
#         myList[i] = base

#         #递归前后半区
#         QuickSort(myList, start, i - 1)
#         QuickSort(myList, j + 1, end)
#     return myList


# myList = [49,38,65,97,76,13,27,49]
# print("Quick Sort: ")
# QuickSort(myList,0,len(myList)-1)
# print(myList)



# 实现快排
def quicksort(nums):
    if len(nums) <= 1:
        return nums
 
    # 左边数组
    left = []
    # 右边数组
    right = []
    # 基准数
    base = nums.pop()
 
    # 对原数组进行划分
    for x in nums:
        if x < base:
            left.append(x)
        else:
            right.append(x)
 
    # 递归调用
    return quicksort(left) + [base] + quicksort(right)
 
if __name__ == '__main__':
    nums = [6,1,2,7,9,3,4,5,10,8]
    quicksort(nums)

