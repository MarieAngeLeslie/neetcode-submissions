class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_bound, rigth_bound = 0, len(nums)-1
        

        while left_bound < rigth_bound :
            middle = (left_bound + rigth_bound)//2
            
            if(nums[middle] > nums[rigth_bound] ) :
                left_bound = middle + 1
            else :
                rigth_bound = middle

        return nums[rigth_bound] 
        #at the end, left_bound == right_bound 