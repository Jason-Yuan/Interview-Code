##############################################################################################################################
# Ideas: directly calculate the two probabilities of each game
# Time Complexity: O(1)
# Space Complexity: O(1)
##############################################################################################################################

def chooseGame(p):
	"""
	@param p: probability of one shot
	@return: an integer
	"""
	game1 = p
	game2 = pow(p, 3) + 3 * (1 - p) * pow(p, 2)
	return 1 if  game1 >= game2 else 2

##############################################################################################################################

def main():
	p1 = 0.5
	p2 = 0.8
	print "If p is {}, choose game {}".format(p1, chooseGame(p1))
	print "If p is {}, choose game {}".format(p2, chooseGame(p2))

if __name__ == '__main__':
	main()