class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def dp(n, k):
            if k == 0: return 1
            if n == 1 or k < 0: return 0
            return dp(n, k-1) + dp(n-1, k) - dp(n-1, k-n)
        return dp(n, k) % (10**9+7)
        
        