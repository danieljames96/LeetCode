# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hash_map = {}
        i = 0
        node = head
        while node:
            hash_map[i] = node.val
            node = node.next
            i+=1
        
        n = i
        max_sum = 0

        for i in range(n//2):
            max_sum = max(max_sum, hash_map[i] + hash_map[n-i-1])

        return max_sum