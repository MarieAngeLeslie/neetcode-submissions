class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, len(nums)-1

        while left_pointer < right_pointer : 
            mid = ( left_pointer + right_pointer ) // 2
            if nums[mid] > nums[right_pointer] : 
                left_pointer = mid + 1
                
            if nums[mid] < nums[right_pointer] :
                right_pointer = mid
            
        return nums[left_pointer]
        