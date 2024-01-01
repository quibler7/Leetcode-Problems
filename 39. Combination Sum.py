class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # define backtracking function
        def backtrack(start, target, path, res):
            if target < 0: return 
            if target == 0:
                res.append(path)
                return 
            for i in range(start, len(candidates)):
                backtrack(i, target-candidates[i], path+[candidates[i]], res)
        
        res = []
        backtrack(0, target, [], res)
        return res

               