# Link: https://leetcode.com/problems/hamming-distance/description/
# Difficulty: Easy
# Problem # 461

# Copilot got this one for me...
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers and count the number of 1's in the result
        print(f'{x}: {bin(x)}, {y}: {bin(y)}')
        
        print(bin(x)[2:].zfill(8), bin(y)[2:].zfill(8))
        print(bin(x ^ y)[2:].zfill(8))

        return bin(x ^ y).count('1')
        

if __name__ == "__main__":

    s = Solution()
    print(s.hammingDistance(1, 4))  # Output: 2
    print(s.hammingDistance(3, 1))  # Output: 1
    print(s.hammingDistance(4, 4))  # Output: 0
    print(s.hammingDistance(0, 0))  # Output: 0