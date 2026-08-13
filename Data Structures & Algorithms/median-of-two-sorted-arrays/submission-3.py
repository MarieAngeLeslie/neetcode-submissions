class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)

        if len(merged_array)%2 != 0 :
            mid = ( 0 + len(merged_array) - 1 ) // 2
            return merged_array[mid]
        else : 
            mid = ( 0 + len(merged_array) - 1 ) // 2
            median = (merged_array[mid] + merged_array[mid+1])/2
            return median