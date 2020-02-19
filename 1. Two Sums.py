# Approach 1: Brute Force O(N^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1) :
            for j in range(i+1, len(nums)) :
                if nums[i]+nums[j] == target :
                    return [i, j]

# Approach 2: Hash Maps O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i, n in enumerate(nums) :
            if differences.get(n) == None :
                differences[target-n] = i
            else :                
                return [differences[n], i]