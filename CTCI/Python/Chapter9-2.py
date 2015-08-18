##############################################################################################################################
# Ideas: Dynamic Programing
# Time Complexity: O(x*y)
# Space Complexity: O(x*y)
##############################################################################################################################

def findPath(m, n):
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for j in range(n+1): dp[0][j] = 1
        for i in range(m+1): dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

##############################################################################################################################

def main():
	a = 3
	b = 3
	print "Number of unique path from (0, 0) to ({},{}) is {}".format(a, b, findPath(a, b))

if __name__ == '__main__':
	main()