class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers)-1


        while left_pointer != right_pointer :
            sum_ = numbers[left_pointer] + numbers[right_pointer]


            if sum_ == target :
                return [left_pointer+1, right_pointer+1]
               
            if sum_ > target :
               right_pointer-=1
            else :
                left_pointer+=1
