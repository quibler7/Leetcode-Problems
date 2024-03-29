class Solution:

    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxnum = max(nums)
        ans = 0
        n = len(nums)

        # Store the indices of the maximum elements
        maxind = [i for i in range(n) if nums[i] == maxnum]

        # Size of the maxind list
        indsize = len(maxind)
        # Iterate through maxind to create windows of size k
        for i in range(indsize - k + 1):
            # Define the end index of the current window
            end = i + k - 1
            # Calculate 'l' (number of elements to the left of the window)
            l = maxind[i] if i == 0 else maxind[i] - maxind[i - 1] - 1
            # Calculate 'r' (number of elements to the right of the window)
            r = n - 1 - maxind[end]
            # Add the number of subarrays possible for the current window to the answer using the subarr function
            ans += (l+1)*(r+1)
        return ans