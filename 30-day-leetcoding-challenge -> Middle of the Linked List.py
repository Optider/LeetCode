# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        count = 0
        while temp :
            count += 1
            temp = temp.next
        temp = head
        count = int(count/2)
        while count :
            count -= 1
            temp = temp.next
        return temp
