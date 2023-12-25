class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # similar to 'linked list cycle 2'

        slow, fast = nums[0], nums[0]
        while True:
            slow,fast = nums[slow], nums[nums[fast]]
            if slow == fast: break
        
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        
        return slow
        