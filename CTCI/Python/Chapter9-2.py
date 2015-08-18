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

# Follow up, with obstacles
def findPathWithObs(m, n, obstacles = None):
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        temp1 = temp2 = 1
        for j in range(n+1):
            if (0, j) in obstacles:
                temp1 = 0
            dp[0][j] = temp1
        for i in range(m+1):
            if (i, 0) in obstacles:
                temp2 = 0
            dp[i][0] = temp2
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (i, j) in obstacles:
                    dp[i][j] = 0
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

##############################################################################################################################

def main():
    a = [(1, 0), (1, 1)]
    print "Number of unique path from (0, 0) to ({},{}) is {}".format(3, 3, findPath(3, 3))
    print "Number of unique path from (0, 0) to ({},{}) with obstacles is {}".format(3, 3, findPathWithObs(3, 3, a))

if __name__ == '__main__':
	main()