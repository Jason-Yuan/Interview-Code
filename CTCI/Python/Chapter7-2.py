##############################################################################################################################
# Ideas: directly calculate the two probabilities of each game
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def collisionProbability(n):
	return (1 - pow(0.5, n))

##############################################################################################################################

def main():
	n = 6
	print "Chance of {} vertexs is {}".format(n, collisionProbability(n))

if __name__ == '__main__':
	main()
