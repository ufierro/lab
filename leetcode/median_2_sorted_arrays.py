import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = []
        a, b = 0, 0
        while a < len(nums1) and b < len(nums2) :
            if nums1[a] < nums2[b]:
                s.append(nums1[a])
                a+=1
            else:
                s.append(nums2[b])
                b+=1
        s_f = s + nums1[a:] + nums2[b:]
        if len(s_f) % 2 == 1:
            return float(s_f[math.floor((len(s_f)+1)/2-1)])
        else:
            u = s_f[math.floor(len(s_f)/2)]
            l = s_f[math.floor(len(s_f)/2-1)]
            return (float(u+l)) / 2