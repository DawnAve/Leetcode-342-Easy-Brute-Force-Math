class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>=4:
            n = n/4
        return n==1

#beets 34.62% runtime and 8.52% memory
