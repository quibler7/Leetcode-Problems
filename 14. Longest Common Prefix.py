class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        ans = ""
        s.sort()
        first = s[0]
        last = s[-1]

        for i in range(min(len(first), len(last))):
            # if first and last th strings first char is not matching
            # then there is no common prefix 
            # return ""
            if first[i] != last[i]: return ans
            # we found first prefix
            ans += first[i]
        
        return ans

        