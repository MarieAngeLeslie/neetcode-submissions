class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        rigth_pointer = len(nums) - 1

        while ( left_pointer <= rigth_pointer ) : 
            middle = (rigth_pointer + left_pointer)//2

            if (target < nums[middle] ) :
                rigth_pointer = middle -1 
                continue
            
            if (target > nums[middle] ) : 
                left_pointer = middle + 1
                continue

            return middle

        return -1