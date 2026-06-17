class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l,r = 1,length-2
        while l<=r:
            m = (l+r)//2
            left,mid,right = mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)
            if left<mid<right:
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        peak = m
        
        l=0
        r=peak
        while l<=r:
            new_m = (l+r)//2
            mid = mountainArr.get(new_m)
            if mid == target:
                return new_m
            elif mid<target:
                l=new_m+1
            else:
                r=new_m-1
                
        
        l=peak
        r=length-1
        while l<=r:
            new_m = (l+r)//2
            mid = mountainArr.get(new_m)
            if mid == target:
                return new_m
            elif mid<target:
                r=new_m-1
            else:
                l=new_m+1
        return -1

            