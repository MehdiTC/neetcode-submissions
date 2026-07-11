# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        i = 0
        n = []
        for node in lists:
            if node:
                heapq.heappush(n, (node.val, i, node))
            i+=1

        while n:
            minn = heapq.heappop(n)[2]
            if minn.next:
                heapq.heappush(n, (minn.next.val, i, minn.next))
                i+=1
            curr.next = minn
            curr = curr.next
        
        return dummy.next
            
        