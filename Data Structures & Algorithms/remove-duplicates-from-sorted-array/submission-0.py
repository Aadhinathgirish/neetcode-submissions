class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i+=1
            else:
                nums[k]=nums[i+1]
                k+=1
                i+=1
        return k