class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i, a in enumerate(nums) : 
            if a > 0 :
                break
            
            if i > 0 and a == nums[i-1] : 
                continue

            left_pointer, right_pointer = i+1, len(nums)-1

            while left_pointer < right_pointer : 

                if a + nums[left_pointer] + nums[right_pointer] > 0 : 
                    right_pointer -= 1
                    continue
                    

                if a + nums[left_pointer] + nums[right_pointer] < 0 : 
                    left_pointer += 1
                    continue

                output.append([a,nums[left_pointer],nums[right_pointer]])
                left_pointer += 1
                right_pointer -= 1
                while nums[left_pointer] == nums[left_pointer-1] and left_pointer < right_pointer :
                    left_pointer+=1
        return output





