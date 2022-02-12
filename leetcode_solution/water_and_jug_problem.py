class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
    
        return z == 0 or ((z <= x + y ) and (z % gcd(x, y) == 0))
        
