# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Difficulty: Hard
# Name: Reverse Nodes in k-Group

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List

def arrayToList(arr: List[int])->ListNode:
    count = 0
    head = None
    if not arr:
        return ListNode()
    else:
        while arr:
            val = arr.pop(0)
            if count == 0:
                head = ListNode(val)
                count += 1
                head_copy = head
            else:
                head.next = ListNode(val)
                head = head.next

        copy2 = head_copy
        while copy2:
            print(copy2.val)
            copy2 = copy2.next

    return head_copy

                



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        head = arrayToList(head)
        head_copy = head
        k_counter = 0

        def inner_step(node, k_counter, k):
            if k_counter > k:
                return None
            elif node:
                step_collection.append(node)
                k_counter += 1
                inner_step(node.next, k_counter, k)
            else:
                return None

        first_pass = True
        while head:
            step_collection = []
            if first_pass:
                inner_step(head, k_counter, k)
                print(step_collection)
                step_collection.reverse()
                head_copy = step_collection[0]
                for index in range(len(step_collection)):
                    if index == len(step_collection)-1:
                        break
                    else:
                        step_collection[index].next = step_collection[index+1]
                first_pass = False
                k_counter = 1
                while k_counter <= k:
                    head = head.next
                    k_counter += 1
                k_counter = 1
            else:
                inner_step(head, k_counter, k)
                print(step_collection)
                step_collection.reverse()
                for index in range(len(step_collection)):
                    if index == len(step_collection)-1:
                        break
                    else:
                        step_collection[index].next = step_collection[index+1]

                k_counter = 1
                while k_counter <= k:
                    head = head.next
                    k_counter += 1
                k_counter = 1
        
        return head_copy



if __name__ == "__main__":
    S = Solution()
    inputs = [([1, 2, 3, 4, 5], 2), ([1, 2, 3, 4, 5], 3)]

    x = arrayToList(inputs[0][0])
    while x:
        print(x.val)
        x = x.next
    
    for inp in inputs:
        print(S.reverseKGroup(head=inp[0], k=inp[1]))

