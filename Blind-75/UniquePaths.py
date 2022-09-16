class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # kinda want to use a bottom up approach
        # want to use a 2D array for this problem
        
        # my general theory for this problem is that for every entry in the 2D array, I want dp[m][n] = dp[m-1][n] + dp[m][n-1]
        # EXCEPT for the case where m=1 or n=1 (in that case it's just going to be set to 1)
        # I proved it to myself on paper that this will work for both the examples given in the problem. dp[m-1][n-1] will contain the answer
        dp = [[1] * n] * m
        
        # so this is actually the first dp problem I was able to get first try, super easily
        # one thing I took from the solution was initializing the whole array by 1. That way, I didn't need to check for the outer row/columns and initialize it to 1. That pruned the 2D array by n+m cells (it made it about 10% faster on leetcode)
        for row in range(1, m):
            for column in range(1, n):
                # if row == 0 or column == 0:
                #     dp[row][column] = 1
                # else:
                dp[row][column] = dp[row-1][column] + dp[row][column-1]
        return dp[m-1][n-1]
