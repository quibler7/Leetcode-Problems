class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i, ele in enumerate(nums):

            if ele in d: return True

            d[ele] = i
        
        return False
        