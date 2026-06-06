class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contain = set()
        r,l=0,0
        res=0
        while r <len(s):
            if s[r] in contain:
                contain.remove(s[l])
                l+=1
            
            else:
                contain.add(s[r])
                r+=1
                m = r - l
                res = max(res,m)

        return res


        