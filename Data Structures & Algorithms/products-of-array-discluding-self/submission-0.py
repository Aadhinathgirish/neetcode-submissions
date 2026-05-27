class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            k=0
            res=1
            for k in range(len(nums)):
                if i!=k:
                    res *= nums[k]
            output.append(res)
        return output
                