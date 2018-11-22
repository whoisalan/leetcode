# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        mid = head
        while node:
            if node.next:
                node = node.next
            else:
                return mid
            if node.next:
                node = node.next
            else:
                mid = mid.next
                return mid
            mid = mid.next
        
        return mid

# simplified:
def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow