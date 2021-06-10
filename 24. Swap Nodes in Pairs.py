# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while cur.next and cur.next.next:
            first = cur.nex #initializing the first node 
            sec = cur.next.next #initialiing the second node
            cur.next = sec #then we let the seond node become the node after the dummy node
            first.next = sec.next #then we let the node originally after the second node become connected to the first node
            sec.next = first
            cur = cur.next.next
        return dummy.next     
        
