# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:16:05 2022

@author: SwarnaRavali
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:22:52 2022

@author: SwarnaRavali
"""

# Definition for singly-linked list.
def print_ll(rev):
    while rev is not None:
        print(rev.val)
        rev = rev.next
        
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseLinkedList(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next
            
            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr
            
            # Move on to the next node
            ptr = next_node
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
    
    def reverselist(self, l1,k):
       if l1 is None:
           return None
       
       new_head = None
       ptr = l1
       while k:
           next_node = ptr.next
           ptr.next = new_head
           new_head = ptr
           ptr = next_node
           k-=1
           
       return new_head
   
    def reversekgroup(self,l1,k):
        count = 0
        ptr = l1
        
        while count < k and ptr:
            ptr = ptr.next
            count += 1
            
        if count == k:
            reverse_head = self.reverselist(l1, k)
            l1.next = self.reversekgroup(ptr, k)
            return reverse_head
        return l1

class Solution1:
    
    def reverseLinkedList(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head
        while k:
            
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next
            
            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr
            
            # Move on to the next node
            ptr = next_node
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
                
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        ptr = head
        ktail = None
        
        # Head of the final, moified linked list
        new_head = None
        
        # Keep going until there are nodes in the list
        while ptr:
            count = 0
            
            # Start counting nodes from the head
            ptr = head
            
            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # If we counted k nodes, reverse them        
            if count == k:
                
                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList(head, k)
                
                # new_head is the head of the final linked list
                if not new_head:
                    new_head = revHead
                
                # ktail is the tail of the previous block of 
                # reversed k nodes
                if ktail:
                    ktail.next = revHead
                    
                ktail = head 
                head = ptr
        
        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head
        
        return new_head if new_head else head

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(5)
l1.next.next.next.next = ListNode(6)
l1.next.next.next.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

Sol = Solution1()
rev = Sol.reverseKGroup(l1,2)
print_ll(rev)