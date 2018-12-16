def binSearch(list1,key1):
    i,j = 0,len(list1)-1
    
    while i<=j :
        mid = (i+j)//2
        if key1<list1[mid]:
            j = mid-1
        elif key1>list1[mid]:
            i = mid+1
        else:return mid
    
    return -1