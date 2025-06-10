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

        
if __name__ == "__main__":
    M = MergeTree()
    nums1 = [1, 45, 99, 8900, 40005]
    nums2 = [1, 2, 4, 7, 10, 840, 8009, 999999]
    while nums1 and nums2:
        if nums1[0] > nums2[0]:
            item = nums2.pop(0)
        else:
            item = nums1.pop(0)
        print(item)
        M.insert(item)

    if nums1:
        for item in nums1:
            M.insert(item)
    else:
        for item in nums2:
            M.insert(item)

    print(M._data)
    print(M.median())

