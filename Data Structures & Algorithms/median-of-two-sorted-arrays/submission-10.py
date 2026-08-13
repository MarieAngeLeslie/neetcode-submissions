class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_array_len, second_array_len = len(nums1), len(nums2)
        i = j = 0
        previous_median = current_median = 0

        for count in range( (first_array_len + second_array_len)//2 + 1) : 

            previous_median = current_median

            if i < first_array_len and j < second_array_len: 
                if nums1[i] < nums2[j] : 
                    current_median = nums1[i]
                    i += 1
                elif nums1[i] > nums2[j] : 
                    current_median = nums2[j]
                    j += 1
                else : 
                    current_median = nums1[i]
                    i += 1

            elif i < first_array_len  : 
                current_median = nums1[i]
                i += 1

            elif j < second_array_len  :
                current_median = nums2[j]
                j += 1

        if (first_array_len + second_array_len) % 2 == 1:
            return current_median
        else :
            return (previous_median+current_median)/2
