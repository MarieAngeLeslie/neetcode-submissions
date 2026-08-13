class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values_dic = { }
        array_length = len(nums)
        final_array =[ ]

        for i in range (array_length) :
            values_dic[nums[i]] = values_dic.get(nums[i],0) + 1

        if ( i == array_length-1) :
            count = k
            while count !=0 :
                max_key = max ( values_dic,  key = values_dic.get)
                final_array.append(max_key)
                del values_dic[max_key]
                count-=1

        return final_array