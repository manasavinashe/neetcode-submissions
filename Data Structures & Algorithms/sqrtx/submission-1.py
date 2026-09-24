class Solution:
    def mySqrt(self, x: int) -> int : 
        l = 1 
        r = x 
        res = 0

        while l <= r :
            mid = (l + r)//2 
            if mid*mid == x : 
                res = mid
                break
            if mid*mid < x :
                l = mid + 1 
                res = mid
            if mid*mid > x : 
                r = mid - 1 
        return res
        
