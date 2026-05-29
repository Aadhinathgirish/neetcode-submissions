class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      curSum = 0
      res=0
      prefix={0:1}
      for i in nums:
        curSum += i
        diff = curSum - k
        res+= prefix.get(diff,0)
        prefix[curSum] = 1 + prefix.get(curSum,0)
      return res


