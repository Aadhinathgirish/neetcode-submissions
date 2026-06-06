class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = 0
        output = len(nums)+1
        for r in range(len(nums)):
            res += nums[r]
            while res >= target:
                length =r-l+1
                output = min(length,output)
                res-=nums[l]
                l+=1
        if output == len(nums)+1:
            return 0
        else:
            return output
            
