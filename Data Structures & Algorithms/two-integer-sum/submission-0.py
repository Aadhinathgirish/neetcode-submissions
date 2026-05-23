class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chechker = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in chechker:
                return [chechker[diff],i]
            chechker[n]=i
        return