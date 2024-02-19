class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #if n is less than zero then it cant be power of two
        #so return False
        if n <= 0: return False
        #count number of 1's in binary of given number
        #if count is 1 then it means it is a power of two
        #so return True
        return bin(n).count('1') == 1
