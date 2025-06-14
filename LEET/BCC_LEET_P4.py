# Median of Two Sorted Arrays
# Difficulty: Hard
# https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
LOL - Either they have made these easier or IDK.  Just got a hard one without cheating and looking at the answers!!!

I don't think it actually meets the requirement of  O(log(m+n)) though....  
"""

class MergeTree:
    """
    This answer was 50ms and 18.52 MB memory, so not good at all.  Worst category in both.  

    However, first time getting a hard done without help so I will pat myself on the back for this low hanging fruit.
    """
    def __init__(self):
        self._data = []
    
    def insert(self, *args):
        for item in args:
            self._data.append(item)
            self._back_correct()

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _back_correct(self):
        if len(self._data) < 2:
            pass
        elif self._data == 2:
            if self._data[0] >= self._data[1]:
                self._swap(0, 1)
        else:
            j = len(self._data)-1
            i = len(self._data)-2
            while i >= 0 and self._data[j] <= self._data[i]:
                self._swap(i, j)
                i -= 1
                j -= 1
    
    def __str__(self):
        for item in self._data:
            print(item)
        return None
    
    def median(self):
        mid = len(self._data) // 2
        if len(self._data) % 2 == 0:
            return (self._data[mid-1]+self._data[mid]) / 2
        else:
            return self._data[mid]
        
# Best Answer - https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/4070500/99-journey-from-brute-force-to-most-optimized-three-approaches-easy-to-understand/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):


        n1 = len(nums1) #7
        n2 = len(nums2) #18
        
        # Ensure nums1 is the smaller array for simplicity
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n = n1 + n2 # total length for odd/even calculation
        # 25
        left = (n1 + n2 + 1) // 2 # Calculate the left partition size 'actual' index position for median
        # 13

        low = 0
        high = n1 # setting the high limit on the total length of the smaller array
        
        while low <= high:
            mid1 = (low + high) // 2 # Calculate mid index for nums1
            mid2 = left - mid1 # Calculate mid index for nums2

            # Infinite placeholders in case end of bounds are reached
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            
            # Determine values of l1, l2, r1, and r2
            if mid1 < n1:
                r1 = nums1[mid1]
                #r1 is the middle value of nums1
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                # The partition is correct, we found the median
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # We are trying to include less from nums1, so we need to move left
                # Move towards the left side of nums1
                high = mid1 - 1
            else:
                # Move towards the right side of nums1
                # We are trying to include more from nums1, so we need to move right
                low = mid1 + 1
        
        return 0 # If the code reaches here, the input arrays were not sorted.

        
if __name__ == "__main__":
    # My answer test
    # M = MergeTree()
    nums1 = [1, 45, 99, 8900, 40005, 41000, 42999]
    nums2 = [1, 2, 4, 7, 10, 840, 8009, 999999, 1000000, 1000001, 1000002, 1000003, 1000004, 1000005, 1000006, 1000007, 1000008, 1000009]
    # region MyAnswer
    # while nums1 and nums2:
    #     if nums1[0] > nums2[0]:
    #         item = nums2.pop(0)
    #     else:
    #         item = nums1.pop(0)
    #     print(item)
    #     M.insert(item)

    # if nums1:
    #     for item in nums1:
    #         M.insert(item)
    # else:
    #     for item in nums2:
    #         M.insert(item)

    # print(M._data)
    # print(M.median()
    # endregion

    S = Solution()
    S.findMedianSortedArrays(nums1, nums2)

