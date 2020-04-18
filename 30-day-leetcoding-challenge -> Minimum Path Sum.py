class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        length = len
        try :
            row = length(grid)
            col = length(grid[0])
        except :
            return 0
        
        # THIS method is alot FASTER ##########################

        for i in range(1, row) :
            grid[i][0] += grid[i-1][0]
            
        for j in range(1, col) :
            grid[0][j] += grid[0][j-1]
            
        for i in range(1, row) :
            for j in range(col) :
                grid[i][j] += min( grid[i-1][j] + grid[i][j-1] )        
        
        return grid[row-1][col-1]
    
#     ALTER working
        
#         for i in range(row):
#             for j in range(col):
                
#                 if i == 0 and j ==0 :
#                     continue
                
#                 if i-1<0:
#                     grid[i][j] += grid[i][j-1]
#                 if j-1 < 0 :
#                     grid[i][j] += grid[i-1][j]
#                 if i !=0 and j != 0 :
#                     grid[i][j] += min( grid[i-1][j], grid[i][j-1] )
                
#         return grid[row-1][col-1]
