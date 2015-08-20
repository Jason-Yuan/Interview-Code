##############################################################################################################################
# Ideas: Recursion 
#        e.g.                          amount = 26
#                     26 (cur = 10)                    1(cur = 10)
#     26 (cur=5)      16 (cur=5)     6 (cur=5)
#  26 (cur=1) 21(cur=5) ......     
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def findChange(availableChanges, amonut):
  if amonut == 0:
    return 1

  if amonut < 0 or not availableChanges:
    return 0

  curChange = availableChanges[-1]
  return findChange(availableChanges[:-1], amonut) + findChange(availableChanges, amonut - curChange)

##############################################################################################################################

def main():
	availableChanges = [1, 5, 10, 25]
	amonut = 26
	print "Num of possibility for {} cents is: {}".format(amonut, findChange(availableChanges, amonut))

if __name__ == '__main__':
	main()