class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_seq = 0
        numSet = set(nums)

        for n in numSet:
            if (n-1) not in numSet:
                
                # start of seq
                curr_num, curr_seq = n, 1
                while (curr_num + 1) in numSet:
                    curr_num += 1
                    curr_seq += 1
                
                long_seq = max(curr_seq, long_seq)
        
        return long_seq
    