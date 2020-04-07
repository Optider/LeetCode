import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize-1
        new_sum = -sys.maxsize

        for i in range(len(nums)) :    
            new_sum = max( new_sum+nums[i], nums[i] )
            max_sum = max( max_sum, new_sum )
        return max_sum
