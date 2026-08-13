
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_pointer, right_pointer = 0, len(heights)-1
        biggest_container = 0

        while left_pointer < right_pointer : 
            possible_biggest_container = (right_pointer - left_pointer) * min(heights[left_pointer], heights[right_pointer])
            biggest_container = max(possible_biggest_container, biggest_container)

            if heights[left_pointer] < heights[right_pointer] : 
                left_pointer += 1
            else : 
                right_pointer-=1

        return biggest_container