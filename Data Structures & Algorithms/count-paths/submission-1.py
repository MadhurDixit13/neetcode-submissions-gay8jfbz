class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dyn = [] 
        for i in range(0, m+1):
            temp = []
            for j in range(0,n+1):
                temp.append(0)
            dyn.append(temp)
            
        dyn[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dyn[i][j] = dyn[i+1][j] + dyn[i][j+1] + dyn[i][j]
        return dyn[0][0]

