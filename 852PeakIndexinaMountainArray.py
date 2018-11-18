# golden section search!

def peakIndexInMountainArray(self, A):
    return A.index(max(A))

def peakIndexInMountainArray(self, A):
    l, r = 0, len(A) - 1
    while l < r:
        mid = (l + r) / 2
        if A[mid] < A[mid + 1]:
            l = mid
        elif A[mid - 1] > A[mid]:
            r = mid
        else:
            return mid