class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        removed = 0
        for i in range(len(nums)) :
            if nums[i-removed] == 0 :
                nums.pop(i-removed)
                nums.append(0)
                removed += 1
