class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        for i in count:
            if count[i] > 1:
                return i
        
        