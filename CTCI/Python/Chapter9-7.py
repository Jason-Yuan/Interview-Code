##############################################################################################################################
# Ideas: Recursion, DFS 
# Time Complexity: O(m * n)
# Space Complexity: O(1)
##############################################################################################################################

def paintFill(screen, x, y, oldColor, newColor):
	if x <0 or x>len(screen[0])-1:
		return
	if y<0 or y>len(screen)-1:
		return
	if screen[x][y] == oldColor:
		screen[x][y] = newColor
		paintFill(screen, x-1, y, oldColor, newColor) # left
		paintFill(screen, x+1, y, oldColor, newColor) # right
		paintFill(screen, x, y-1, oldColor, newColor) # bottom
		paintFill(screen, x, y+1, oldColor, newColor) # top

# help method, print image
def printImage(img):
	for row in img:
		print row

##############################################################################################################################

def main():
	screen = [[0,0,0,0,0],[0,1,1,1,0],[0,1,1,0,0],[1,1,0,1,0],[0,1,1,1,0]]
	print "Original Image"
	printImage(screen)
	paintFill(screen, 2, 2, 1, 5)
	print "New Image"
	printImage(screen)

if __name__ == '__main__':
	main()