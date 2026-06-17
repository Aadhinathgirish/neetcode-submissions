class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarry = 0
            curSum =0
            for n in nums:
                curSum+=n
                if curSum>largest:
                    subarry+=1
                    curSum = n
            return subarry+1 <= k
        l=max(nums)
        r=sum(nums)
        res = r
        while l<=r:
            mid = (l+r)//2
            if canSplit(mid):
                res = mid
                r = mid-1
            else:
                l=mid+1
        return res
        