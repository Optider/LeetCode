# Solution 1: using two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(0, len(nums)-1) :
            if nums[j] != nums[j+1] :
                nums[i+1] = nums[j+1]
                i += 1
        return i+1

# Solution 2: using Hash Table
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = {}
        i = 0
        for idx, val in enumerate(nums) :
            if unique.get(val) == None :
                unique[val] = idx
                nums[i] = val
                i += 1
        return i

# Little Faster than Sol 2
# Solution 3: using Hash Table BUT wihout enumerate since index is not needed
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = {}
        i = 0
        for val in nums :
            if unique.get(val) == None :
                unique[val] = True
                nums[i] = val
                i += 1
        return i
