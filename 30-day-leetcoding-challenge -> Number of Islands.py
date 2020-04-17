class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        try :
            m = len(grid)
            n = len(grid[0])
        except :
            return 0
        count = 0
        
        
        for row in range(m) :
            for col in range(n) :
                
                if grid[row][col] == '0' :
                    continue
                queue = []
                
                queue.append((row, col))
                
                grid[row][col] = '0'
                
                while queue :
                    i, j = queue.pop(0)
                    # for a, b in (i+1, j), (i-1, j), (i, j-1), (i, j+1) :
                    for x, y in (i-1, j), (i+1, j), (i, j-1), (i, j+1) :
                    
                        if 0<=x<m and 0<=y<n and grid[x][y] == '1' :
                            grid[x][y] = '0'
                            queue.append((x, y))
                            
                count += 1        
        return count
