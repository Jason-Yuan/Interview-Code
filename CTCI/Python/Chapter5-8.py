##############################################################################################################################
# Ideas: 1. calculate which row should we draw the line, and draw a rough line first
#        2. clean the head pixels
#        3. fill the tail pixels
# Time Complexity: O(width)
# Space Complexity: O(1)
##############################################################################################################################

def drawLine(screen, width, x1, x2, y):
	if width % 8 != 0:
		return
	if x1 < 0 or x2 < 0 or x1 > width or x2 > width or x1 > x2:
		return
	height = len(screen) / (width / 8)
	if y < 0 or y > height:
		return

	start_pix = (width * y) + x1
	end_pix = (width * y) + x2

	# draw a rough line 
	for i in range(start_pix / 8, end_pix / 8):
		screen[i] |= 0xFF

	# clean the head pixels
	screen[start_pix / 8] &= (0xFF >> (x1 % 8))

	# fill the tail pixels
	screen[end_pix / 8] |= ((0xFF << (8 - (x2 % 8))) & 0xff)
	return

def printScreen(screen, width):
	cur = 0
	while cur < len(screen):
		for i in range(width / 8 - 1):
			print "{:08b}".format(screen[cur]),
			cur += 1
		print "{:08b}".format(screen[cur])
		cur += 1

##############################################################################################################################

def main():
	screen = [0b00000000 for i in range(8)]
	drawLine(screen, 16, 3, 13, 2)
	printScreen(screen, 16)

if __name__ == '__main__':
	main()