class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         newhash = {}
         list1 =[[]for i in range(len(nums)+1)]
         for n in nums:
            newhash[n] = 1 + newhash.get(n,0)
         for n,c in newhash.items():
             list1[c].append(n)
         res=[]
         for i in range(len(list1)-1,0,-1):
            for j in list1[i]:
                res.append(j)
                if len(res)==k:
                    return res
         