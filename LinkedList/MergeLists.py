# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = cur = ListNode(None)
        while h:
            val, idx = heapq.heappop(h)
            cur.next = ListNode(val)
            cur = cur.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(h, (node.val, idx))
        return head.next
    
Sol = Solution()

l1 = ListNode(5)
l1.next = ListNode(6)
l1.next.next = ListNode(7)

l2 = ListNode(1)
l2.next = ListNode(4)

l3 = ListNode(3)
l3.next = ListNode(5)

lists = [l1,l2,l3]
Sol.mergeKLists(lists)