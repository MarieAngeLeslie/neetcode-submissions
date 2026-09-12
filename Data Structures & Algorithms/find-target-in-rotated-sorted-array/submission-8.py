class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer, right_pointer = 0, len(nums)-1 
        pivot = 0
        while left_pointer < right_pointer : 
            middle = (left_pointer+right_pointer)//2
            if nums[middle] > nums[right_pointer] :
                left_pointer = middle+1
            if nums[middle] < nums[right_pointer] :
                right_pointer = middle

        pivot = left_pointer #pivot contain the index here of most smallest element

        def binary_search(left:int, right:int)->int:
            while left <= right : 
                middle = (left+right)//2
                if target < nums[middle] : 
                    right = middle - 1
                if target > nums[middle] : 
                    left = middle + 1
                if target == nums[middle] :
                    return middle
            return -1

        target_index = binary_search(0, pivot-1)
        if target_index != -1 :
            return target_index

        return binary_search(pivot, len(nums)-1)



