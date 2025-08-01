# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Difficulty: Medium
# Name: Swap Nodes in Pairs

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Time: 0ms - Beats 100% - 
    Space: 18.04 MB - Beats 11.59%
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        count = 0
        
        while curr and curr.next:
            if count == 0:
                f = curr.next
                b = f.next 
                curr.next = b
                f.next = curr
                head = f
                count += 1
            elif count % 2 != 0 and curr.next.next:
                f = curr.next.next 
                b = curr.next
                b.next = f.next if f.next else None
                f.next = b
                curr.next = f
                count += 1
                curr = curr.next
            else:
                curr = curr.next
                count += 1
            p_l = []
            head_copy = head
            while head_copy:
                p_l.append(head_copy.val)
                head_copy = head_copy.next
            print(p_l)
            head_copy = head
        
        return head




if __name__ == "__main__":
    S = Solution()
    one = ListNode(1)
    two = ListNode(2)
    thr = ListNode(3)
    four = ListNode(4)
    head = one
    one.next = two
    two.next = thr
    thr.next = four
    head2 = None
    head3 = ListNode(1)
    
    x = S.swapPairs(head)
    while x:
        print(x.val)
        x = x.next
    print(x)
    