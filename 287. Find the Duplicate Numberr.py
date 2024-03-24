class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # set slow and fast pointer to nums[0]
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            # break when they become equal
            if slow == fast: break

        # set slow pointer to start again
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

