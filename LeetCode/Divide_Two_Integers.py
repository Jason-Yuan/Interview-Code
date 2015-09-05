class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT
        sign = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        q = 1
        dvs = divisor
        while dvs < dividend:
            dvs = dvs << 1
            q = q << 1
        while dvs >= divisor:
            if dividend >= dvs:
                dividend -= dvs
                res += q
            q = q >> 1
            dvs = dvs >> 1
        res = res if sign else -res
        return min(res,MAX_INT)