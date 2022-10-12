class Solution(object):
    def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         setNums = set()

#         for n in nums:
#             if n in setNums:
#                 setNums.discard(n)
#             else:
#                 setNums.add(n)
        
#         return setNums.pop()
            
    
    #O(1) SPACE COMPLEXITY
    
        result = 0 
        for i in nums:
            result = result ^ i #xor???   
            
        return result
