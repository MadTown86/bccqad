#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Difficulty: Medium
# Name: Remove Nth Node From End Of List

# Definition for singly-linked list.

from typing import List

# Node Class - Singly-Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Quick function to convert input list into singly-linked list
def listToNode(nums: List[int]) -> ListNode:
    if not nums:
        return ListNode(val=None, next=None)
    else:
        head = ListNode(val=nums.pop(0))
        node = head
        for i in nums:
            new_node = ListNode(val=i)
            node.next = new_node
            node = node.next

    return head


from typing import Optional
class Solution:
    """
    Time: 0ms - 100% Beat
    Space: 17.6MB - 86% Beat
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head = listToNode(head)
        i = []
        node = head
        while node:
            i.append(node)
            node = node.next

        if len(i) == n:
            head = head.next
        else:
            before = len(i)-(n+1)
            after = before + 2 
            i[before].next = i[after] if after < len(i) else None

        # node = head
        # while node:
        #     print(f'NODE VAL: {node.val}')
        #     node = node.next

        return head

if __name__ == "__main__":
    S = Solution()
    #
    inputs = [([1,2,3,4,5],2), ([1],1), ([1, 2], 1), ([1, 2], 2)]

    for inp in inputs:
        print(S.removeNthFromEnd(*inp))