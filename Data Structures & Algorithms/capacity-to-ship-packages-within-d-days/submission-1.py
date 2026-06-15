class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res = r
        def canShip(cap):
            curr = cap
            ship = 1
            for w in weights:
                if curr - w < 0:
                    ship+=1
                    curr = cap
                curr-=w
            return ship<=days
        while l<=r:
            cap = (l+r)//2
            if canShip(cap):
                res = min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res