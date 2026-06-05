class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        contain = {}
        for i,n in enumerate(nums):
            if n in contain :
                if abs(contain[n]-i) <= k:
                    return True
            contain[n] = i
        return False        