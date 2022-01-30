class Solution:
    def Maximum_Sum(self, mat, N, K):
        # Your code goes here
        
        # prefix matrix
        for i in range(N):
            for j in range(N):
                if i-1 >= 0:
                    mat[i][j] += mat[i-1][j]
                if j-1 >= 0:
                    mat[i][j] += mat[i][j-1]
                if i-1 >= 0 and j-1>= 0:
                    mat[i][j] -= mat[i-1][j-1]
                    
        ans = float('-inf')
        # sum of k matrix:
        for i in range(N):
            for j in range(N):
                local = mat[i][j]
                if i-K >=0:
                    local -= mat[i-K][j]
                if j-K >= 0:
                    local -= mat[i][j-K]
                if i-K >=0 and j-K>=0:
                    local += mat[i-K][j-K]
                ans = max(ans, local)
                    
        return ans
    
mat = [[1, 1, 1, 1, 1], 
[2 ,2 ,2, 2, 2], 
[3, 8, 6, 7, 3], 
[4, 4, 4, 4, 4], 
[5, 5, 5, 5, 5]]
N =5
K = 3

print(Solution().Maximum_Sum(mat, N, K))
                    