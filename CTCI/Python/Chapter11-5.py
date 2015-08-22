##############################################################################################################################
# Ideas:	1. Similar like binary search
#       	2. If we met "", keep mid + 1 until its not "" or mid > end
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
##############################################################################################################################

def searchString(strList, str):
	if str == "":
		return -1

	start = 0
	end = len(strList) - 1
	while start <= end:
		mid = (start + end) / 2
		if strList[mid] == str:
			return mid

		temp = mid
		while temp <= end and strList[temp] == "":
			temp += 1
		if temp > end: # which means the right part are all ""
			end = mid - 1
		else:
			if strList[temp] > str:
				end = mid - 1
			elif strList[temp] < str:
				start = temp + 1
			else:
				return temp

	return -1

##############################################################################################################################

def main():
	a = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
	string = "ball"
	print "Find {} in {}\nThe index number is: {}".format(string, a, searchString(a, string))
	a = ["at", "", "", "", "ball", "", "", "", "", "", "", "", ""]
	string = "ball"
	print "Find {} in {}\nThe index number is: {}".format(string, a, searchString(a, string))
	a = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
	string = "dad"
	print "Find {} in {}\nThe index number is: {}".format(string, a, searchString(a, string))

if __name__ == '__main__':
	main()