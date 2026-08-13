class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        first_left_pointer, first_right_pointer = 0, ROWS-1

        while first_left_pointer <= first_right_pointer :
            true_array = first_left_pointer + (first_right_pointer - first_left_pointer) // 2

            if target < matrix[true_array][0] :
                first_right_pointer = true_array - 1
                continue
                
            if target > matrix[true_array][-1] :
                first_left_pointer = true_array + 1
                continue
                
            break

        if first_left_pointer > first_right_pointer : 
            return False

        true_array = first_left_pointer + ( first_right_pointer - first_left_pointer) // 2
        second_left_pointer, second_right_pointer = 0, COLS-1

        while second_left_pointer <= second_right_pointer :
            middle = second_left_pointer + ( second_right_pointer - second_left_pointer) // 2

            if target < matrix[true_array][middle] :
                second_right_pointer = middle - 1
                continue
            
            if target > matrix[true_array][middle] :
                second_left_pointer = middle + 1
                continue
            
            return True
        
        return False


