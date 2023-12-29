class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l = 0
        # sliding window 

        for r in range(len(s)):
            # when we encounter duplicate element
            while s[r] in charSet:
                # keep removing left char 
                # keep incrementing left pointer 
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, (r-l+1))
        
        return res
        