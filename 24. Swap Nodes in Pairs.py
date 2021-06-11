# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#recursion
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
            sec.next = first #then we let the first node become connected to the second node now the first node
            cur = cur.next.next #then we point to the 3rd pointer 
        return dummy.next     
#iteration
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        temp=head
        while temp is not None and temp.next is not None:
            temp.val,temp.next.val=temp.next.val,temp.val
            temp=temp.next.next
        return head
        
