# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        
        main = head
        new_head = None
        while main != None:
            next_node = main.next
            main.next = new_head
            new_head = main            
            main = next_node
            
        return new_head
            
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(6)
l1.next.next.next.next.next = ListNode(7)
r1 = Solution().reverseList(l1)

while r1 != None:
    print(r1.val, end=" ")
    r1 = r1.next