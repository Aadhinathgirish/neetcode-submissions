class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,k,j= m-1,n-1,len(nums1)-1
        while i >= 0 and k >=0:
            if nums1[i]>nums2[k]:
                nums1[j]=nums1[i]
                j-=1
                i-=1
            elif nums1[i]<nums2[k]:
                nums1[j] = nums2[k]
                j-=1
                k-=1
            else:
                 nums1[j] = nums1[i]
                 i-=1
                 j-=1
                 k-=1
        while j >=0:
                if k>=0:
                    nums1[j]=nums2[k]
                    k-=1
                j-=1
        return nums1




       