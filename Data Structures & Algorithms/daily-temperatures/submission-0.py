class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       final_result = [0] * len(temperatures) 
       temperatures_stack = []
       for i, elt in enumerate(temperatures) : 
            while (temperatures_stack and elt > temperatures_stack[-1][1]) : 
                current_elt_popped = temperatures_stack.pop()
                final_result[current_elt_popped[0]] = i -  current_elt_popped[0]
            temperatures_stack.append((i, elt))
       return final_result
                