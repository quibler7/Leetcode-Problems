class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for n in range(len(nums)):
            if nums[n] == val:
                nums[n] = 101
                c += 1
        nums.sort()
        
        return len(nums) - c
        