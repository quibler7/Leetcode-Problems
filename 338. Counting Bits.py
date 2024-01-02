class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(0, n+1):
            ele = bin(i).count('1')
            res.append(ele)
        return res
        