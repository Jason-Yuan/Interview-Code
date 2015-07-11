# Find more about substring search algorithm from /Interview-Code/SubString Search

# so for this problem we just use Brute Force algorithm to search the substring
# also in python, we can simply do "if s1 in s2" to check if s1 is a substring of s2

def IsSubtring(string, pattern):
	for i in range(len(string)-len(pattern)+1):
		result = True
		for j in range(len(pattern)):
			if pattern[j] != string[i+j]:
				result = False
		if result:
			return True
	return False
# end define

##############################################################################################################################
# Method 1
# Ideas: If s2 is a rotation of s1, the s2 must be a sub string of s1+s1
# Time Complexity: O(m*n) based on the IsSubstring method
# Space Complexity: O(n)
##############################################################################################################################

def IsRotation(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		concat_s1 = s1 + s1
		if IsSubtring(concat_s1, s2):
			return True
		else:
			return False

##############################################################################################################################

def main():
	s1 = "waterbottle"
	s2 = "erbottlewat"
	print "Is {} a rotation of {} ?".format(s2, s1)
	print IsRotation(s1, s2)

if __name__ == '__main__':
	main()