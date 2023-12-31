class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1

        for l in range(len(s)):
            for r in range(l+1, len(s)):
                if s[l] == s[r]:
                    res = max(res, r-l-1)
        
        return res
        