##############################################################################################################################
# Ideas:	1. First sort by height
#       	2. Similar like longest increasing subsequence(LIS) problem
# Issue:	If the people has same heights, we should not continue counting
# Time Complexity: O(n ^ 2)
# Space Complexity: O(n)
##############################################################################################################################

class person(object):
	def __init__(self, height, weight):
		self.height = height
		self.weight = weight
	def __str__(self):
		return "({}, {})".format(self.height, self.weight)
		
def longestTower(A):
        B = sorted(A, key=lambda person: person.height)
        dp = [1 for i in range(len(B))]
        for i in range(1, len(B)):
            for j in range(i):
                if B[i].weight > B[j].weight and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
        return max(dp)

##############################################################################################################################

def main():
	people = [person(65, 100), person(68, 110), person(56, 90), person(75, 190), person(60, 95), person(70, 150)]
	print "The highest tower has {} people.".format(longestTower(people))

if __name__ == '__main__':
	main()