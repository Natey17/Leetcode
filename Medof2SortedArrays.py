class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        list3 = []
        
        for x in nums1:
            list3.append(x)
        for x in nums2:
            list3.append(x)
        list3.sort()

        n = len(list3)

        if n % 2 == 0:
            median = ((list3[n // 2 - 1] + list3[n // 2]) / 2)
        else:
            median = list3[(n) // 2]
        return median