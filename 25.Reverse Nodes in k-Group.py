# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Example:

# Given this linked list: 1->2->3->4->5

# For k = 2, you should return: 2->1->4->3->5

# For k = 3, you should return: 3->2->1->4->5

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        first = head
        second = head
        flag = 1
        def reverse(head):
            if head == None:
                return None
            if head.next == None:
                return head, head
            
            root, curr = reverse(head.next)
            # print(root, curr, head)
            curr.next = head
            head.next = None
            return root, head
        
        while first:
            ctr = 1
            while ctr<k:
                ctr+=1 
                second = second.next
                if second == None:
                    return head
                
            pivot = second.next
            second.next = None
            
            # print(second)
            if flag:
                flag=0
                first, second = reverse(head)
                second.next = pivot
                head = first
                first = pivot
                prev = second
                second = pivot
                # print(first, prev)
                continue
            # print(first)
            first, second = reverse(first)
            prev.next = first
            second.next = pivot
            prev = second
            first = pivot
            second = pivot
        return head
            
            
