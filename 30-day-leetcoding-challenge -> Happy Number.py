class Solution:
    def isHappy(self, n: int) -> bool:
        n_str = str(n)
        visited = set()
        
        while not n_str in visited :
            visited.add(n_str)
            
            # loop through str(n)
            new_sum = 0
            # for every letter find its sq and add to sum
            for s in n_str :
                new_sum += int(s)**2

            # if sum is 1 retrun True
            if new_sum == 1 :
                return True
            
            n_str = str(new_sum)
            print(visited)
            
        else :
            return False
