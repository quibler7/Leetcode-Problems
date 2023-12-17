class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                # elements before nums[i] are unique so
                nums[i] = nums[j]
        return i + 1



        