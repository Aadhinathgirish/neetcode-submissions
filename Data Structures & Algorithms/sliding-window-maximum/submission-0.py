class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r = k-1
        output = []
        for l in range(len(nums)-k+1):
            res = nums[l:r+1]
            value = max(res)
            output.append(value)
            r+=1
        return output

        