class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for i in range(numRows):
            a = []
            for j in range(i+1):
                if j == 0 or j == i:
                    a.append(1)
                else: 
                    a.append(res[i-1][j-1]+res[i-1][j])
            res.append(a)
        
        return res

        