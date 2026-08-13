
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights)-1
        biggest_container = 0
        minimum_height = 0

        while left_pointer < right_pointer : 

            if heights[left_pointer] < heights[right_pointer] : 
                minimum_height = heights[left_pointer]
            else : 
                minimum_height = heights[right_pointer]

            possible_biggest_container = (right_pointer - left_pointer) * minimum_height
            biggest_container = max(possible_biggest_container, biggest_container)

            if heights[left_pointer] < heights[right_pointer] : 
                left_pointer += 1
            else : 
                right_pointer-=1


        return biggest_container