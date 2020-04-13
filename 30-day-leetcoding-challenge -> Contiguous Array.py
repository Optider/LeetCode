class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c,d,m = 0,{0:0},0 # Defined vars
        for i,v in enumerate(nums): # scanning through the array
            c += 2*v -1 # +1 if v ==1 or -1 if v==0
            if c in d: # have we seen that count of 0/1s before?
                m = max(m,i+1-d[c]) # was that subarray longer?
            else:
                d[c] = i+1        # no, this is the first time, let's add that index for that c        
        return m  # return the largest length ...
