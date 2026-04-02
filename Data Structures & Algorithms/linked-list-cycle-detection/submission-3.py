# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastptr = None
        slowptr = None
        if head!= None: 
            if head.next!=None:
                slowptr = head.next
        if slowptr!=None:
            fastptr = slowptr.next
        while fastptr!=None:
            if slowptr == fastptr:
                return True
            if slowptr!=None:
                slowptr = slowptr.next
                if fastptr.next!=None:
                    fastptr = fastptr.next.next
                else: 
                    break
            else:
                break
        return False