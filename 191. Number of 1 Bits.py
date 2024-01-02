class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n != 0:
            res += (n%2) # either 0 or 1 will get added
            n >>= 1
        
        return res
        