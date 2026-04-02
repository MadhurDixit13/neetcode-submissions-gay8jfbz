
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        p = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = p
            p = curr
            curr = temp
            
        head = p
        return head
        
