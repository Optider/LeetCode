class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
                
        stones.sort()
        for i in range(len(stones)-1, 0, -1) :
            stones[i-1] = abs(stones[i-1] - stones[i])
            stones.sort()
        return stones[0]
