##############################################################################################################################
# Ideas: first a ^ b, then calculate how many 1 are there 
# Time Complexity: O(n)
# Space Complexity: O(n)
##############################################################################################################################

def findMissing(A):
    return findMissingRecur(A)

def findMissingRecur(A):
    if sum(A) == 0: return 0
    zeros, ones = [], []
    for a in A:
        if (a&1)==1:
            a>>=1
            ones.append(a)
        else:
            a>>=1
            zeros.append(a)
    if len(zeros) <= len(ones):
        # LSB of x is 0
        v = findMissingRecur(zeros)
        return (v<<1)|0
    else:
        # LSB of x is 1
        v = findMissingRecur(ones)
        return (v<<1)|1

##############################################################################################################################

def main():
    a = [0,1,2,3,4,5,7,8,9,10]

    print a
    print "Missing: ", findMissing(a)

if __name__ == '__main__':
    main()