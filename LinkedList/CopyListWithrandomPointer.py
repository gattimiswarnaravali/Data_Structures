# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited_dict = {}
    
    def copyRandomList(self, head):
        if head == None:
            return None
        
        if head in self.visited_dict:
            return self.visited_dict[head]
        
        node = Node(head.val, None,None)
        self.visited_dict[head] = node
        
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node
    
    def getClonedNode(self, node):
        if node is None:
            return None
        
        if node in self.visited_dict:
            return self.visited_dict[node]
        else:
            self.visited_dict[node] = Node(node.val, None,None)
            return self.visited_dict[node]    
        
        return None
    
    def copyRandomList(self, head):
        if head is None:
            return None
        
        old_head = head
        new_head = self.getClonedNode(old_head)
        
        while old_head != None:
            new_head.random = self.getClonedNode(old_head.random)
            new_head.next = self.getClonedNode(old_head.next)
            
            old_head = old_head.next
            new_head = new_head.next
            
        return self.visited_dict[head
    
class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new
                