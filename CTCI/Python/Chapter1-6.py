# define a print image method
def ShowImage(image):
	for row in image:
		print row
# end define

##############################################################################################################################
# Method 1 
# Ideas: First method is really intuitive, but the space complexity is n2.
#        Just copy the input matrix to the result matrix
# Time Complexity: O(n2)
# Space Complexity: O(n2)
##############################################################################################################################

def ImageRotate1(image):
	img_size = len(image)
	# make an same size of "image" to hold the result later
	result = [[0 for i in range(img_size)] for j in range(img_size)]

	# for each pixel of the image copy them to the result image
	for row in range(img_size):
		for col in range(img_size):
			result[col][img_size-row-1] = image[row][col]

	return result

##############################################################################################################################
# Method 2 
# Ideas: Rotate each circle from outside to inside, inplace rotate
# Time Complexity: O(n2)
# Space Complexity: O(1)
##############################################################################################################################

# Rotate 90 degree (clockwise):
# [1, 2, 3]            [7, 4, 1]
# [4, 5, 6]   = = >    [8, 5, 2]
# [7, 8, 9]            [9, 6, 3]

def ImageRotate2(image):
	img_size = len(image)

	# rotate each cicle from outside to inside
	for row in range(img_size/2):
		for col in range(row, img_size-row-1):
			temp = image[row][col]
			image[row][col] = image[img_size-col-1][row]
			image[img_size-col-1][row] = image[img_size-row-1][img_size-col-1]
			image[img_size-row-1][img_size-col-1] = image[col][img_size-row-1]
			image[col][img_size-row-1] = temp

	return image		

##############################################################################################################################
# Method 3 
# Ideas: First transpose, then reverse the rows, shown below
# Time Complexity: O(n2)
# Space Complexity: O(1)
##############################################################################################################################

# [1, 2, 3]     transpose       [9, 6, 3]    reverse the row    [7, 4, 1]
# [4, 5, 6]   =============>    [8, 5, 2]   =================>  [8, 5, 2]
# [7, 8, 9]                     [7, 4, 1]					    [9, 6, 3]

def ImageRotate3(image):
	img_size = len(image)

	# transpose the image by top right to bottom left diagonal
	for row in range(img_size-1):
		for col in range(0, img_size-row-1):
			image[row][col], image[img_size-col-1][img_size-row-1] = image[img_size-col-1][img_size-row-1], image[row][col]

	return image[::-1]


##############################################################################################################################

def main():
	image = [[1, 2, 3],
	         [4, 5, 6],
	         [7, 8, 9]]

	print "Original image"
	ShowImage(image)
	print "Rotate image method 1: "
	ShowImage(ImageRotate1(image))
	print "Rotate image method 2: "
	ShowImage(ImageRotate2(image))
	print "Rotate image method 3: "
	ShowImage(ImageRotate3(image))

if __name__ == '__main__':
	main()