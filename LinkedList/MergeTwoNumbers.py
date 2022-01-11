# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:22:52 2022

@author: SwarnaRavali
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
                
        while l1 or l2:            
            if l1 is None and l2 is None:
                break
            if l1 is None:
                result_tail.next = l2
                break
            if l2 is None:
                result_tail.next = l1
                break
                
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            
            if val1 <= val2:
                current_val = val1
                l1 = (l1.next if l1 else None)
            else:
                current_val = val2
                l2 = (l2.next if l2 else None)
            
            result_tail.next = ListNode(current_val)
            result_tail = result_tail.next                  
            
               
        return result.next
    
    def mergeRecursive(self, l1,l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        head = None
        if l1.val <= l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
            
        head.next = self.mergeRecursive(l1, l2)
        
        return head
    
    def mergeiterative(self, l1,l2):
        head = ListNode(0)
        tail = head
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
            
        tail.next = l1 if l2 is None else l2
        return head.next
    
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

Sol = Solution()
print(Sol.mergeiterative(l1, l2))